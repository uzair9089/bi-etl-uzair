from sqlalchemy import create_engine
from threading import Thread, Lock
import pandas as pd
import threading
import psycopg2
import os
import jira.client
from jira.client import JIRA
import etl_delta_load as etl
import sys

reload(sys)
sys.setdefaultencoding('utf8')

conn_string = os.environ['conn_bi']
conn = psycopg2.connect(conn_string)
curs = conn.cursor()

user = os.environ['jira_user']
password = os.environ['jira_pass']

options = {'server': 'https://jira.shore.com'}
jira = JIRA(options, basic_auth=(user, password))
projects = jira.projects()
#issues = jira.search_issues("updated >= -2w  order by created DESC", startAt=0, maxResults=20000, validate_query=True, fields=None, expand='changelog,customfield', json_result=None)
issues = jira.search_issues("updated >= -2d and updated < -1d  order by created DESC", startAt=0, maxResults=2000, validate_query=True, fields=None, expand='changelog,customfield', json_result=None)

for i in projects:
        curs.execute("insert into jira.map_issues(project_id, project_name,etl_date) values('{0}','{1}',current_date)".format(i.key,i.name))
        conn.commit()

# for issues and to track their history in life time
for i in issues:
        issue = jira.issue(i)
        changelog = issue.changelog
        for history in changelog.histories:
                for item in history.items:
                        #print item.field
                        if item.field == 'status':
                                #print i.key,issue.fields.status,issue.fields.timeestimate, issue.fields.description,issue.fields.summary, issue.fields.priority , issue.fields.assignee, issue.fields.status, issue.fields.labels, issue.fields.created, issue.fields.updated,issue.fields.issuetype, issue.fields.creator
                                curs.execute("insert into jira.issues_history (timeestimate,description,status_changed,history,summary, priority, assignee, status, labels, created, updated, issuetype, creator, issue_id, etl_date) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}'::timestamp,'{10}'::timestamp,'{11}','{12}','{13}', current_date)"
                                .format(issue.fields.timeestimate,issue.fields.description.replace("'","") if issue.fields.description   else issue.fields.description,history.created , ' From:' + item.fromString + ' To:' + item.toString,str(issue.fields.summary).replace("'",""), issue.fields.priority , issue.fields.assignee, issue.fields.status, str(issue.fields.labels).replace("'",""), issue.fields.created, issue.fields.updated,issue.fields.issuetype, issue.fields.creator, i.key))
                                curs.execute("update jira.issues set project_id ={0}".format("substring(issue_id,1,position('-' in issue_id)-1)"))
                                conn.commit()

# For issues which are still in the backlog
for i in issues:
        issue = jira.issue(i)
        curs.execute("insert into jira.issues (timeestimate,description,summary, priority, assignee, status, labels, created, updated, issuetype, creator, issue_id, etl_date) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}'::timestamp,'{8}'::timestamp,'{9}','{10}','{11}', current_date)"
        .format(issue.fields.timeestimate,issue.fields.description.replace("'","") if issue.fields.description   else issue.fields.description,str(issue.fields.summary).replace("'",""), issue.fields.priority , issue.fields.assignee, issue.fields.status, str(issue.fields.labels).replace("'",""), issue.fields.created, issue.fields.updated,issue.fields.issuetype, issue.fields.creator, i.key))
        curs.execute("update jira.issues set project_id ={0}".format("substring(issue_id,1,position('-' in issue_id)-1)"))
        conn.commit()

# story point
for i in issues:
        try:
                curs.execute("insert into jira.issue_story_points(issue_id, points, etl_date) values('{}','{}', current_date)".format(i,i.fields.customfield_10006))
                conn.commit()
        except AttributeError:
                curs.execute("insert into jira.issue_story_points(issue_id, points, etl_date) values('{}','{}', current_date)".format(i,'N/A'))
                conn.commit()

# sprint information
for i in issues:
        if i.fields.customfield_10001:
                for item in i.fields.customfield_10001:
                        try:
                                #print item, i
                                curs.execute("insert into jira.sprints(issue_id, sprint_info, etl_date) values ('{0}','{1}',current_date)".format(str(i), item))
                                conn.commit()
                        except AttributeError:
                                pass
        else:
                curs.execute("insert into jira.sprints(issue_id, sprint_info, etl_date) values ('{0}','{1}', current_date)".format(str(i), 'N/A'))
                conn.commit()

# run the required transformation after the importing all data
for keys in etl.query:
        curs.execute(etl.query[keys])
        conn.commit()

conn.close()
curs.close()
