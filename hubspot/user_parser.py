from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
from etl_delta_load import delta_query
import psycopg2
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class UserParser:

  def parser(self, collection_name):

    try:

      conn_string = param.conn_bi
      conn = psycopg2.connect(conn_string)
      curs = conn.cursor()

      if collection_name in param.truncate_queries:
        curs.execute(param.truncate_queries[collection_name])
        curs.execute
        conn.commit()

      file = open(param.newpath+collection_name,'r')

      for line in file:
        x = json.loads(line,strict=False) 
        keys_in_record = x.keys() 
        #print keys_in_record

        if 'data' in keys_in_record:

          for data_lines in x["data"]:
            id =  company = email = status = language = first_login = first_name  = last_name = ics_link = location_id = 'N/A' 
            created = modified = activation_due_date = '9999-01-01'
            
            if '_id' in data_lines.keys():
              id = str(data_lines["_id"]).replace("'","")
              #print id

            if 'company' in data_lines.keys():
              company = data_lines["company"]
              #print company

            if 'email' in data_lines.keys():
              email = data_lines["email"].replace("'","")
              #print status

            if 'status' in data_lines.keys(): 
              status = str(data_lines["status"]).replace("'","")
              #print invoice_month

            if 'language' in data_lines.keys():
              language = str(data_lines["language"]).replace("'","")
              #print language

            if 'firstLogin' in data_lines.keys():
              first_login = str(data_lines["firstLogin"]).replace("'","")
              #print first_login

            if 'lastName' in data_lines.keys():
              last_name = str(data_lines["lastName"]).replace("'","")
              #print last_name

            if 'icsLink' in data_lines.keys():
              ics_link = data_lines["icsLink"]
              #print ics_link

            if 'locationId' in data_lines.keys():
              location_id = str(data_lines["locationId"]).replace("'","")
              #print location_id


            curs.execute("insert into absence.users(id, company, email, status, language, first_login, first_name, last_name, ics_link, location_id, created, modified, activation_due_date) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')"
            .format(id, company, email, status, language, first_login, first_name, last_name, ics_link, location_id, created, modified, activation_due_date))

            conn.commit()

      print("finished parsing data for: " + collection_name)

      print ("delta load starts ")

      curs.execute(delta_query['users'])
      conn.commit()

    except Exception as e:
      param.counter-1
      print ("exception")
      conn.rollback()
      curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
      .format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e).replace("'",""), 'fail'))
      conn.commit()
      conn.close()
      curs.close()

    finally:
      conn.close()
      curs.close()