"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: connect to the BI server and import csv files into respective tables.
"""

from absences_parser import AbsencesParser as ap
from company_parser import CompanyParser as cp
from reasons_parser import ReasonsParser as rp
from invoice_parser import InvoiceParser as ip
from user_parser import UserParser as up
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

        # improt the company object
        if self.collection_name == 'company.json':
            if param.newpath + self.collection_name:
                do = cp()
                do.parser(self.collection_name)
                print "finished parsing data for: " + self.collection_name
        # import the invoice object
        if self.collection_name == 'invoices.json':
            if param.newpath + self.collection_name:
                do = ip()
                do.parser(self.collection_name)
                print "finished parsing data for: " + self.collection_name
        # import the users object
        if self.collection_name == 'users.json':
            do = up()
            do.parser(self.collection_name)
            print("finished parsing data for: "+ self.collection_name)
        # import the absences object
        if self.collection_name == 'absences.json':
            if param.newpath + self.collection_name:
                print param.newpath + self.collection_name
                do = ap()
                do.parser(self.collection_name)
                print "finished parsing data for: " + self.collection_name
        # imp the reason object 
        if self.collection_name == 'reasons.json':
            if param.newpath + self.collection_name:
                do = rp()
                do.parser(self.collection_name)
                print "finished parsing data for: " + self.collection_name
        # history load
        if self.collection_name[:-5] in param.temp_objects:
            if param.newpath + self.collection_name:
                do = rp()
                do.parser(self.collection_name)
                print "finished parsing data for: " + self.collection_name
        else:
            print "no matching file found"

def import_data():
    for key, values in param.exported_file.iteritems():
        if(param.exported_file[key] == 1):
            print("importing data into table: " + key)
            runner = Importer(key + '.json')
            param.exported_file[key] = 0
            param.counter = param.counter - 1
            print param.counter
            runner.start()
            
















