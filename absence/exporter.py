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


class Exporter(Thread):
    __lock = Lock()


    def __init__(self, collection_name):
        Thread.__init__(self)
        self.collection_name = collection_name


    def run(self):


    	try:
            conn_string = param.conn_bi
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()

            print(param.counter)

            if self.collection_name in param.history_objects: 
                response = requests.request("POST", param.url[self.collection_name], data=param.filters[self.collection_name]+str(param.skip_counter)+"\n}"+"sortBy: {\"company\": 1}", headers=param.headers).json()
                print param.filters[self.collection_name]+str(param.skip_counter)+"\n}"
                with open(param.newpath+self.collection_name+'.json', 'w') as outfile:
                    json.dump(response, outfile)

                param.exported_file[self.collection_name] = 1

                param.row_count = int(response['totalCount'])
                param.loop_counter = (param.row_count/param.row_limit) + 2

                param.counter = param.counter + param.loop_counter-1


                for i in range(1, param.loop_counter):
                    param.skip_counter =  i * param.row_limit
                    response = requests.request("POST", param.url[self.collection_name], data=param.filters[self.collection_name]+str(param.skip_counter)+"\n}"+"sortBy: {\"company\": 1}", headers=param.headers).json()
                    print param.filters[self.collection_name]+str(param.skip_counter)+"\n}"
                    with open(param.newpath+self.collection_name + "_" +str(i)+'.json', 'w') as outfile:
                        json.dump(response, outfile)

                        param.temp_objects.append(self.collection_name+"_"+str(i))

                        param.exported_file[self.collection_name+"_"+str(i)] = 1


            else:
                response = requests.request("POST", param.url[self.collection_name], data=param.filters[self.collection_name], headers=param.headers).json()
                with open(param.newpath+self.collection_name+'.json', 'w') as outfile:
                    json.dump(response, outfile)

                param.exported_file[self.collection_name] = 1
                print("extraction completed for: "+ self.collection_name )

    	except Exception as e:

            curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.collection_name, param.root+self.collection_name+str(".json"), 'import', str(e),'fail'])
            conn.commit()
            conn.close()
            curs.close()

        finally:
            conn.close()
            curs.close()






