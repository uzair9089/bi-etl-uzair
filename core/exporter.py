"""
Author: Sanjiv Upadhyaya
Date: 2016-010-03
Function: connect to the prod server and export tables into the csv.
"""

from threading import Thread, Lock
from importer import Importer
import sqlalchemy as sqa
from param import param
import psycopg2.extras
import pandas as pd
import psycopg2


# class implementing threads so CSV can be dumped in parallel
class Exporter(Thread):
    __lock = Lock()


    
    def __init__(self, query, file_name):
        Thread.__init__(self)
        self.file_name = file_name
        self.query = query



    def run(self):
    
        try:
            conn_string = param.connection
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()

            outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(self.query)

            try:
                with open(param.newpath+self.file_name +".csv", 'w+') as f:
                    curs.copy_expert(outputquery, f)

            except Exception as e:
                #conn.rollback()
                curs.execute("""INSERT INTO public.etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.file_name[:-4], param.newpath+self.file_name, 'export', str(e), 'fail'])
                conn.commit()

            param.exported_file[self.file_name] = 1

        except Exception as e:
            print("Unable to access database, export error %s %s" % (str(e), self.file_name))

            conn.rollback()
            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.file_name[:-4], param.newpath+self.file_name, 'export', str(e), 'fail'])
            conn.commit()

        finally:
            curs.close()
            conn.close()
            