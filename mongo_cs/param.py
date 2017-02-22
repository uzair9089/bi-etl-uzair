
"""
Author: Sanjiv Upadhayaya
Date: 2016-10-03
tFunction: hold the parameters of ETL process including database connection, ETL run dates and directory
"""

from datetime import date, timedelta
import datetime
import pprint
import time
import os


class param:		

	schema = "cs"
	root = '/opt/etl/mongo_cs/data/'
	counter = 0 
	newpath = ""
	connection = ""
	st_dt = datetime.datetime.utcnow() - datetime.timedelta(hours = 176)
	st_dt = st_dt.strftime('%Y-%m-%d %H:00:00')
	gmt_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(st_dt, "%Y-%m-%d %H:%M:%S"))))
	st_dt = gmt_dt.replace(' ','T')
	start_date =  str(st_dt) +'Z'
	end_date = datetime.datetime.utcnow() - datetime.timedelta(hours = 1)
	end_date = end_date.strftime('%Y-%m-%d %H:00:00')
	gmt_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(end_date, "%Y-%m-%d %H:%M:%S"))))
	end_date = gmt_dt.replace(' ','T')
	end_date = end_date+'Z'

	# filters
	filters = ["'{updated_at:{$gte:new Date(\"", "\"),$lt:new Date(\"", "\")}}'"]

	tbl_cs= ['customers', 'custom_attribute_definitions']

	# dictionary for storing truncate queries for tables without the date attributes.
	truncate_queries = {
						# example schema--> change it to appropriate table name in future when required
						'example1': "truncate table cs.example1;"
						,'example2': "truncate table cs.eample2;"
						
	}

	# complete list of collections to be extracted from the mongodDB -->> In future we will receive data from absence.io as well.
	tbl_bi = tbl_cs 

	# files ready to be parsed: checked by the import_data module.
	exported_file = dict((el,0) for el in tbl_bi)
	
	conn_cs = os.environ['conn_cs']

	conn_bi = os.environ['conn_bi']

	# allocation of db connection when runner program is executed. 
	@classmethod
	def dbconn(self,host):
		if(host == "cs"):
			param.connection = self.conn_cs
			param.schema = "cs"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'

		else:
			print("Invalid Host given : Please enter the details of the host mongoDB in param.py file ")



