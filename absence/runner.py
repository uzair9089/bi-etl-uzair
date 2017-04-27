"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: main program to run the ETL process.
"""

from exporter import Exporter
from importer import Importer
from param import param
import psycopg2.extras
import threading
import psycopg2
import importer
import datetime
import time
import sys
import os


# argument passed to runner program is stored in host variable
host = sys.argv[1]
#host = "cs"
param.dbconn(host)

if not os.path.exists(param.newpath):
    os.makedirs(param.newpath)


if sys.argv[1] in ('cs', 'absence'):
	print("Extracting Json for " +str(param.start_date) +" - " +str(param.end_date))

else:
	print("No other ETL defiend yet")


if (host == "absence") :
	param.counter = 1
	for i in param.tbl_absence:
	    print('Extracting Json for ' + i +' started')
	    runner = Exporter(i)
	    runner.start()
else:
	print("no other data source is defined yet")

# run the ETL process until all the mentioned collections in the param file are exported.
while param.counter != 0:
	importer.import_data()















