"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: main program to run the ETL process.
"""

from exporter import Exporter
from importer import Importer
from param import param
from time import sleep
import psycopg2.extras
import threading
import psycopg2
#import importer
import datetime
import time
import sys
import os


# argument passed to runner program is stored in host variable
host = sys.argv[1]

param.dbconn(host)

if not os.path.exists(param.newpath):
	os.makedirs(param.newpath)

if sys.argv[1] in ('recurly'):
	print("Extracting Json for " +str(param.start_date) +" - " +str(param.end_date))

else:
	print("No other ETL defined yet")


if (host == "recurly") :
	param.counter = len(param.tbl_recurly)
	for i in param.tbl_recurly:
		print('Extracting Json for ' + i +' started')
		runner = Exporter(i)
		t = runner.start()

else:
	print("no other data source is defined yet")


# run the ETL process until all the mentioned collections in the param file are exported.
i = 0
while i < 10:
	for key, values in param.exported_file.items():
		if os.path.isfile(param.newpath + key + '.csv'):
			param.exported_file['subscriptions'] = 1
			break
		else:
			sleep(10)
			i += 1
	break
#param.counter = 1

for key, values in param.exported_file.items():
	if(param.exported_file[key] == 1):
		print("importing data into table: " + key)
		runner = Importer(key + '.csv')
		param.exported_file[key] = 0
		param.counter = param.counter - 1
		runner.start()