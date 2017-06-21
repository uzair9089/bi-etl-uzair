"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to the BI server and import csv files into respective tables.
"""

from sqlalchemy import create_engine
from threading import Thread, Lock
import etl_delta_load
from param import param
import pandas as pd
import threading
import psycopg2
import boto
import os


# class implementing threading so dumped CSV can be loaded into BI DWH in parallel
class Importer(Thread):
    __lock = Lock()


    def __init__(self, file_name, full_path):
        Thread.__init__(self)
        self.file_name = file_name
        self.full_path = full_path



    def run(self):

        try:

            conn_string = "dbname='segment' port='5439' user='dwhadmin' password='1e14SYTzJoC2H12' host='shore-dwh.ciwq6khdxggb.eu-central-1.redshift.amazonaws.com'"
            #conn_string = param.conn_hash['bi']
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()


            if(self.file_name in param.truncate_tbl):

                curs.execute(etl_delta_load.truncate_queries[self.file_name])

                conn.commit()

            if param.reset_time == param.reset_value and self.file_name not in param.truncate_tbl:
                curs.execute(etl_delta_load.delete_queries[self.file_name])
                conn.commit()
            
            os.environ['S3_USE_SIGV4'] = 'True'
            BUCKET_NAME = param.BUCKET_NAME 
            AWS_ACCESS_KEY_ID = param.AWS_ACCESS_KEY_ID 
            AWS_SECRET_ACCESS_KEY= param.AWS_SECRET_ACCESS_KEY 
            REGION_HOST = param.REGION_HOST 
            conn2 = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY, host = REGION_HOST)
            bucket = conn2.get_bucket(BUCKET_NAME)

            identifier = self.file_name

            for i in bucket:
                #print '/'+i.key
                if self.full_path == '/'+i.key:
                    #print 'entering the copy'
                    print '/'+i.key
                    curs.execute (""" COPY %s.%s FROM 's3://shore-bi-etl/%s' iam_role 'arn:aws:iam::601812874785:role/BIs3Access' fillrecord CSV IGNOREHEADER 1 """ % (param.schema, self.file_name,i.key))
                    curs.execute(etl_delta_load.delta_query[self.file_name])
                    conn.commit()
            #print("delta load for: " +self.file_name +" completed ***")

                #print("import for " +self.file_name +" completed !!!")
                #print("delta load starts for:" +self.file_name)

                    # if param.reset_time == param.reset_value:
                    #     curs.execute(etl_delta_load.delta_query_reset[self.file_name])
                    #     conn.commit()
                    #     #print("delta load for: " +self.file_name +" completed ***RESET***")
                    # else:
                    #     curs.execute(etl_delta_load.delta_query[self.file_name])
                    #     conn.commit()
                    #print("delta load for: " +self.file_name +" completed ***")

                #print("import for " +self.file_name +" completed !!!")
                #print("delta load starts for:" +self.file_name)


        except Exception as e:
            print("Unable to access database, import error %s %s" % (str(e), self.file_name))
            param.counter-1
            conn.rollback()
            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.file_name, param.newpath+self.file_name, 'import', str(e),'fail'])
            conn.commit()
            
        finally:
            curs.close()
            conn.close()


      
# import_data function is called every minute by the runner program until ETL for all the tables are completed  
# Here check the s3 bucket for the files specified and then run the import of the data
def import_data():
    for key, values in param.exported_file.iteritems():
        if(param.exported_file[key] == 1):
            print("importing data into table: " + key)
            runner = Importer(key + '.csv')
            param.exported_file[key] = 0
            param.counter = param.counter - 1
            runner.start()


















