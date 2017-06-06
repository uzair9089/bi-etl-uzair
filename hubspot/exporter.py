from datetime import  date, timedelta
from threading import Thread, Lock
from param import param
import datetime
import dateutil
import psycopg2
import commands
import requests
import pprint
import json
import time
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Exporter(Thread):
    __lock = Lock()




    def __init__(self, collection_name):
        Thread.__init__(self)
        self.collection_name = collection_name


    def run(self):

        self.time_offset = 0
        self.vid_offset = 0

    	try:
            conn_string = param.conn_bi
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()


            if self.collection_name in param.history_objects: 
                response = requests.request("GET", param.url[self.collection_name], headers=param.headers, params = param.recent_querystring).json()
                with open(param.newpath+self.collection_name+'.json', 'w') as outfile:
                    json.dump(response, outfile)

                param.exported_file[self.collection_name] = 1

                self.time_offset = int(response['time-offset'])
                self.vid_offset = int(response['vid-offset'])

                new_url = param.url[self.collection_name]

                #print self.collection_name

                while self.time_offset >= param.previous_date:
                    print "here"
                    response = requests.request("GET", new_url, headers=param.headers, 
                        params= {"hapikey":os.environ['hubspot'], "count":"100000","vidOffset":int(param.vid_offset),"timeOffset":int(param.time_offset)}).json()
                    print int(response['time-offset'])

                    #print ("lets see how long does it las")

                    # param.exported_file[self.collection_name + "_" +str(param.vid_offset)] = 1
                    # self.time_offset = int(response['time-offset'])
                    # self.vid_offset = int(response['vid-offset'])
                    # param.temp_objects.append(self.collection_name+"_"+str(param.vid_offset))

                    # param.new_url = param.url[self.collection_name] + "&vidOffset={0}&timeOffset={1}".format(param.vid_offset,param.time_offset)

                    with open(param.newpath+self.collection_name + "_" +str(param.vid_offset)+'.json', 'w') as outfile:
                         json.dump(response, outfile)

                    #print self.collection_name+"_"+str(param.vid_offset)+" asdfadsf"

                    #print (param.temp_objects)
                    #print param.time_offset
                    #print param.vid_offset

                    #print "everything fine till here"

            else:
                print "entering else but hwy?"
                response = requests.request("GET", param.url[self.collection_name],  headers=param.headers).json()
                with open(param.newpath+self.collection_name+'.json', 'w') as outfile:
                    json.dump(response, outfile)

                param.exported_file[self.collection_name] = 1
                print("extraction completed for: "+ self.collection_name )

    	except Exception as e:

            print e
            #print ("nope here")
            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",['2017-05-31', '2017-05-31', param.schema, self.collection_name, param.root+self.collection_name+str(".json"), 'import', str(e),'fail'])
            conn.commit()
            conn.close()
            curs.close()

        finally:
            conn.close()
            curs.close()






