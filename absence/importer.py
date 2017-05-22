"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to the BI server and import csv files into respective tables.
"""
from company_parser import CompanyParser as cp
from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
import pandas as pd
import threading
import psycopg2
import requests
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

        if self.collection_name == 'company.json':
            print param.newpath+self.collection_name
            if param.newpath+self.collection_name:
                print param.newpath+self.collection_name
                do = cp()
                do.parser(self.collection_name)
                print "finished parsing data"

        if self.collection_name == 'invoices.json':
            print 'create a parser for the invoices object and rest should be fine'


# import_data function is called every minute by the runner program until ETL for all the tables are completed  
def import_data():
    for key, values in param.exported_file.iteritems():
        if(param.exported_file[key] == 1):
            print("importing data into table: " + key)
            runner = Importer(key + '.json')
            param.exported_file[key] = 0
            param.counter = param.counter - 1
            runner.start()
            
















