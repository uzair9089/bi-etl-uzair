"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to the BI server and import csv files into respective tables.
"""
from custom_customer_attribute_parser import CustomCustomerAttributes  as ccap
from customer_parser import CustomerParser as cp
from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
import pandas as pd
import threading
import psycopg2
import os
import sys
import json


reload(sys)
sys.setdefaultencoding('utf8')


class Importer(Thread):
    __lock = Lock()


    def __init__(self, collection_name):
        Thread.__init__(self)
        self.collection_name = collection_name
        

    def run(self):

        if self.collection_name == 'custom_attribute_definitions.json':
            do = ccap()
            do.parser(self.collection_name)

        if self.collection_name == 'customers.json':
            do = cp()
            do.parser(self.collection_name)

        else:
            print("No other collections are imported yet")
         
# import_data function is called every minute by the runner program until ETL for all the tables are completed  
def import_data():
    for key, values in param.exported_file.iteritems():
        if(param.exported_file[key] == 1):
            print("importing data into table: " + key)
            runner = Importer(key + '.json')
            param.exported_file[key] = 0
            param.counter = param.counter - 1
            runner.start()
            













