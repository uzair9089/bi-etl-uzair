
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to BI DWH and import CSV data into tables.
"""

from sqlalchemy import create_engine
from datetime import date, timedelta
from threading import Thread, Lock
from sf_param import param
import etl_delta_load
import pandas as pd
import threading
import psycopg2
import os




class Importer(Thread):
    __lock = Lock()



    def __init__(self, file_name):
        Thread.__init__(self)
        self.file_name = file_name



    def run(self):

        try:
            conn_string = param.conn_bi
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()

            if (os.stat(param.newpath +self.file_name).st_size > 4):
                file = open(param.newpath +self.file_name)

                #curs.execute("drop index if exists stage.idx_"+self.file_name[:-4])
                curs.copy_expert(sql = """ COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ',' """ % ("sfdc." +str(self.file_name[:-4])), file = file)
                conn.commit()

                print("Import for: " +self.file_name[:-4] +" completed !!!")
                print("Delta load for: " +self.file_name[:-4] +" started ...")

                curs.execute(etl_delta_load.delta_query[self.file_name[:-4]])
                conn.commit()

                
                print("Delta load for: " +self.file_name[:-4] +" completed")

            else:
                print("Empty file for: " +self.file_name[:-4])

        except Exception as e:
            print("Unable to access database, import error %s" % str(e))
            param.counter-1

            conn.rollback()
            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, 'sfdc', self.file_name[:-4], param.newpath+self.file_name, 'import', str(e), 'fail'])
            conn.commit()

        finally:  
            curs.close()
            conn.close()

     
# import_data function is called by the runner program until all the objects are taken care by the ETL process       
def import_data():
    for key, values in param.exported_file.iteritems():
        if(param.exported_file[key] == 1):
            print("importing data into table: " + key)
            runner = Importer(key + '.csv')
            param.exported_file[key] = 0
            param.counter = param.counter - 1
            runner.start()
            













