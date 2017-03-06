from datetime import  date, timedelta
from threading import Thread, Lock
from param import param
import datetime
import dateutil
import psycopg2
import commands
import pprint
import time
import os


class Exporter(Thread):
    __lock = Lock()

    counter_run = 1

    def __init__(self, collection_name):
        Thread.__init__(self)
        self.collection_name = collection_name


    def run(self):
    	
    	try:

            conn_string = param.conn_bi
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()
            var = "mongoexport -h {5} --readPreference secondary --collection {7} --out {6}{7}.json  -q {0}{1}{2}{3}{4}".format(param.filters[0], param.start_date, param.filters[1], param.end_date, param.filters[2], param.conn_cs, param.newpath, self.collection_name)
            err =  commands.getstatusoutput(var)
            err
            #print str(param.exported_file[self.collection_name])+" : " + self.collection_name
            # for checking if there was a connection reset by the peer from the mongo replica set
            while self.counter_run != 0:
                if err:
                    param.exported_file[self.collection_name] = 1
                    self.counter_run = 0
                    #print self.counter_run
                    #print str(param.exported_file[self.collection_name])+" : " + self.collection_name


    	except Exception as e:

            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.collection_name, param.root+self.collection_name+str(".json"), 'import', str(e),'fail'])
            conn.commit()
            conn.close()
            curs.close()

        finally:
            conn.close()
            curs.close()






