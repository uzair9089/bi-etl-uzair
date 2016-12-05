
"""
Author: Sanjiv Upadhyaya
Date: 2016-11-29
Function: Google Analytics data extractor
"""

from oauth2client.service_account import ServiceAccountCredentials  
from googleapiclient.errors import HttpError
from googleapiclient import sample_tools  
from apiclient.discovery import build  
from ga_param import param
from httplib2 import Http 
import psycopg2  
import sys
import os


credentials = ServiceAccountCredentials.from_json_keyfile_name('shorebin.json', ['https://www.googleapis.com/auth/analytics.readonly'])
http_auth = credentials.authorize(Http())
service = build('analytics', 'v3', http=http_auth)


def get_api_traffic_query(service, ga_merchant_id):  
  return service.data().ga().get(
    ids = 'ga:' +str(ga_merchant_id),
    start_date=param.start_date,
    end_date=param.end_date,
    metrics='ga:users, ga:sessions, ga:visits, ga:newUsers',
    dimensions='ga:yearMonth, ga:source, ga:pagePath, ga:hostname, ga:sessionCount, ga:deviceCategory'
    )

def get_api_demographics(service, ga_merchant_id):
	return service.data().ga().get(
		ids='ga:' +str(ga_merchant_id),
		start_date =  param.start_date,
		end_date = param.end_date,
		metrics = 'ga:users',
		dimensions = 'ga:usrGender'
		
		)
