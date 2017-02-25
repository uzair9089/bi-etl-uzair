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

param.dbconn(host)

# perform no_op load from postgres so that the json objects are treated as json instead of text or string
psycopg2.extras.register_default_json(loads=lambda x: x)
psycopg2.extras.register_default_jsonb(loads=lambda x: x)

DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: int(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)


if not os.path.exists(param.newpath):
    os.makedirs(param.newpath)



if sys.argv[1] in ('core', 'nwsl', 'msg', 'comm', 'pymt'):
	if param.reset_time == '13':
		print("Running ETL for " +str(param.reset_start_date) +" - " +str(param.reset_end_date))
	else:
		print("Running ETL for " +str(param.start_date) +" - " +str(param.end_date))

elif sys.argv[1] in ('intercom'):
	print("Running ETL for 1 day")

else:
	print("No other ETL defiend yet")



# filter_row/ filter_row_segment is used to filter the data based on the ETL start_date and end_date
if param.reset_time == '13':
	filter_row = " where updated_at >='" +str(param.reset_start_date) +"' and updated_at<'" +str(param.reset_end_date) +"'"
else:
	filter_row = " where updated_at >='" +str(param.start_date) +"' and updated_at<'" +str(param.end_date) +"'"
#filter_row = " "
filter_row_segment =  " where updated_at::date >= current_date::date -1 and updated_at::date < current_date::date "



if (host == "nwsl") :
	param.counter = 2
	for i in param.tbl_nwsl:
	    print('extraction of ' +i +' started')
	    runner = Exporter("select * from " +i +filter_row, i +"_nwsl")
	    runner.start()

	runner_employee = Exporter("select * from newsletter_customers", 'newsletter_customers')
	runner_employee.start()

elif (host == "core"):
	param.counter = 26
	for i in param.tbl_core:
		print('extraction of ' +i +' started')
		runner = Exporter("select * from " +i +filter_row, i)
		runner.start()

	runner_employee = Exporter("select * from employees",'employees')
	runner_employee.start()

	runner_merchant_key_accounts = Exporter("select * from merchant_key_accounts", 'merchant_key_accounts')
	runner_merchant_key_accounts.start()

	runner_merchant_permissions = Exporter("select * from merchant_permissions", 'merchant_permissions')
	runner_merchant_permissions.start()

elif (host == "msg"):
	param.counter = 6
	for i in param.tbl_msg:
		print('extraction of ' +i +' started')
		runner = Exporter("select * from " +i +filter_row, i)
		runner.start()

	runner_employee = Exporter("select * from conversation_senders", 'conversation_senders')
	runner_employee.start()

elif (host == "comm"):
	param.counter = 4
	for i in param.tbl_comm:
		print('extraction of ' +i +' started')
		runner = Exporter("select * from " +i +filter_row, i)
		runner.start()

	runner_merchant = Exporter("select * from merchants", 'merchants')
	runner_merchant.start()

elif (host == "pymt"):
	param.counter = 6
	for i in param.tbl_pymt:
		print('extraction of ' +i +' started')
		runner = Exporter("select * from " +i, i)
		runner.start()

	runner_merchant = Exporter("select * from merchants", 'merchants_pymt')
	runner_merchant.start()

elif (host == "intercom"):
	param.counter = 8 
	for i in param.tbl_intercom:
	    print('extraction of ' +i +' started')
	    runner = Exporter("select * from " +param.schema +"." +i +filter_row_segment, i +"_intercom")
	    runner.start()

	runner_admins_intercom = Exporter("select * from " +param.schema +"." +"admins", 'admins_intercom')
	runner_admins_intercom.start()

	runner_tags_intercom = Exporter("select * from " +param.schema +"." +"tags", 'tags_intercom')
	runner_tags_intercom.start()


# run the ETL process until all the mentioned tables in the param file are exported.
while param.counter != 0:
	importer.import_data()















