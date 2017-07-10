
from oauth2client.service_account import ServiceAccountCredentials  
from googleapiclient.errors import HttpError
from googleapiclient import sample_tools  
from apiclient.discovery import build  
from ga_param import param
from httplib2 import Http 
import pandas as pd
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
            #cursor.execute("""INSERT INTO ga.traffic_absence (year_month, source, page_path, host, session_count, device_category, user_count, sessions, visit_count, newuser_count, start_date) 
            #    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],param.start_date])

             cursor.execute("""INSERT INTO ga.traffic_absence (year_month, user_count, sessions, visit_count, newuser_count, start_date) 
                VALUES(%s, %s, %s)""", [row[0], row[1], row[2], row[3], row[4], param.start_date])
          except Exception as e:
              print("Unable to access database, import error %s ", str(e) )      
      else:
        pass
      #print('No Rows Found for :'+str(merchant))
except Exception as e:
  print("Error in GA data import %s", str(e))

finally:
  conn.commit()
  cursor.close()
  conn.close()

print("Import of google analytics data for traffic completed !!!")
