#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/jira/jira_python.py  >> /tmp/log_jira$$.log 2>&1
mailx -s "ETL Status - Jira" bi-etl@shore.com  < /tmp/log_jira$$.log
cat /tmp/log_jira$$.log >> /opt/etl/jira/logs/log_jira.txt
rm /tmp/log_jira$$.log