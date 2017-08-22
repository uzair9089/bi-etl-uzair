
from oauth2client.service_account import ServiceAccountCredentials  
from googleapiclient.errors import HttpError
from googleapiclient import sample_tools  
from apiclient.discovery import build  
from ga_param import param
from httplib2 import Http 
import time
import pandas as pd
import datetime
import psycopg2  
import sys
import os
import ga

try:
  conn = psycopg2.connect(param.conn_string)
  cursor = conn.cursor()

  tpl_merchant_list = tuple(param.merchant_list)

except Exception as e:
  print("Unable to establish a connection %s", str(e))

print("Importing google analytics data for "+ param.start_date)


try:
  for merchant in tpl_merchant_list:
    if merchant <= 100000 or merchant in param.exclude_list:
      pass
    else:
    #for merchant in param.merchant_list:
      traffic_results = ga.get_api_traffic_query(ga.service, merchant).execute()
      if traffic_results.get('rows', []):
        for row in traffic_results.get('rows'):
          try:
            row[0] = datetime.datetime.strptime(row[0], '%Y%m%d').strftime('%Y-%m-%d')
            cursor.execute("""INSERT INTO ga.traffic_absence (date, device, user_count, session_count, visit_count) 
                VALUES(%s, %s, %s, %s, %s)""", [row[0], row[1], row[2], row[3], row[4]])

          except Exception as e:
              print("Unable to access database, import error %s ", str(e) )      
      else:
        pass
        
except Exception as e:
  print("Error in GA data import %s", str(e))

finally:
  conn.commit()
  cursor.close()
  conn.close()

print("Import of google analytics data for traffic completed !!!")
