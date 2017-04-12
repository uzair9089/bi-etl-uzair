
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to sales force and extract the data into CSV.
          This script uses beatbox for utilizing SOAP API provided 
          by sales force to extract the data. This script also does
          not work with python version > 2.7
"""

from threading import Thread, Lock
from sf_importer import Importer
from sf_param import param
import sqlalchemy as sqa
import psycopg2.extras
import pandas as pd
import psycopg2
import beatbox



class Exporter(Thread):
    __lock = Lock()
    


    def __init__(self, query, table_name,col):
        Thread.__init__(self)
        self.table_name = table_name
        self.query = query



    def run(self):

        try:
            service = beatbox.PythonClient()  
            service.login(param.user_name, param.password)  
            query_result = service.query(self.query)
            records = query_result['records']  
            total_records = query_result['size']  
            query_locator = query_result['queryLocator']  

            
            while query_result['done'] is False and len(records) < total_records:
                query_result = service.queryMore(query_locator)
                query_locator = query_result['queryLocator'] 
                records = records + query_result['records']  


            table = pd.DataFrame(records)
            table.rename(columns = {'type':'object_type'}, inplace= True)


            table.to_csv(param.newpath +self.table_name +'.csv', index=False)

            # for tacking the invalid query locator error from salesforce
            param.exported_table.append(self.table_name)

            param.exported_file[self.table_name] = 1


        except Exception as e:
            print("Unable to access sales force, export error: %s" % str(e))






