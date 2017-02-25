"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to the BI server and import csv files into respective tables.
"""

from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
import etl_delta_load
import pandas as pd
import threading
import psycopg2
import os


# class implementing threading so dumped CSV can be loaded into BI DWH in parallel
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


            if(self.file_name[:-4] in param.truncate_tbl):

                print("truncating table " +self.file_name[:-4])
                
                curs.execute(param.truncate_queries[self.file_name[:-4]])
                conn.commit()

            if param.reset_time == '00':
                curs.execute(etl_delta_load.delete_queries[self.file_name[:-4]])
                conn.commit()
            
            if (os.stat(param.newpath +self.file_name).st_size > 4):
                file = open(param.newpath +self.file_name)

                curs.copy_expert(sql = """ COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ',' """ % (param.schema +'.' +self.file_name[:-4]), file = file)
                conn.commit()

                print("import for " +self.file_name[:-4] +" completed !!!")
                print("delta load starts for:" +self.file_name[:-4])

                if param.reset_time == '00':
                    curs.execute(etl_delta_load.delta_query_reset[self.file_name[:-4]])
                    conn.commit()
                    print("delta load for: " +self.file_name[:-4] +" completed ***RESET***")
                else:
                    curs.execute(etl_delta_load.delta_query[self.file_name[:-4]])
                    conn.commit()
                    print("delta load for: " +self.file_name[:-4] +" completed ***")

            else:
                print("Empty file for: " +self.file_name[:-4])

        except Exception as e:
            print("Unable to access database, import error %s %s" % (str(e), self.file_name[:-4]))
            param.counter-1

            conn.rollback()
            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.file_name[:-4], param.newpath+self.file_name, 'import', str(e),'fail'])
            conn.commit()
            
        finally:
            curs.close()
            conn.close()



          
# import_data function is called every minute by the runner program until ETL for all the tables are completed  
def import_data():
    for key, values in param.exported_file.iteritems():
        if(param.exported_file[key] == 1):
            print("importing data into table: " + key)
            runner = Importer(key + '.csv')
            param.exported_file[key] = 0
            param.counter = param.counter - 1
            runner.start()
            













