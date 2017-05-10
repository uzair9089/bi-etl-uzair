
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

	schema = ""
	#root = '/Users/sanjivupadhyaya/Desktop/mars1/etl/absence/data'
	root = '/opt/etl/absence/data'
	counter = 0 
	newpath = ""
	connection = ""
	# st_dt = datetime.datetime.utcnow() - datetime.timedelta(hours = 10)
	# st_dt = st_dt.strftime('%Y-%m-%d %H:00:00')
	# gmt_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(st_dt, "%Y-%m-%d %H:%M:%S"))))
	# st_dt = gmt_dt.replace(' ','T')
	# start_date =  str(st_dt) +'Z'
	# start_date = start_date[:10]
	# end_date = datetime.datetime.utcnow() - datetime.timedelta(hours = 1)
	# end_date = end_date.strftime('%Y-%m-%d %H:00:00')
	# gmt_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(end_date, "%Y-%m-%d %H:%M:%S"))))
	# end_date = gmt_dt.replace(' ','T')
	# end_date = end_date+'Z'
	# end_date = end_date[:10]
	start_date = str(date.today() - timedelta(1))
	end_date = str(date.today())



	tbl_absence= ['company']

	url = "https://app.absence.io/api/v2/bi/companies"

	#filters = "{\n\t\"limit\": 10000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n }\n}"
	
	filters = "{\n\t\"limit\" : 10000\n}"

	# move the token to the environment variable somehow
	headers = {
	    'x-vacationtoken': os.environ['x_vacationtoken'],
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': os.environ['postman_token']
	    }


	# dictionary for storing truncate queries for tables without the date attributes.
	truncate_queries = {
						# example schema--> change it to appropriate table name in future when required
						'example1': "truncate table cs.example1;"
						,'example2': "truncate table cs.eample2;"
						
	}

	# complete list of collections to be extracted from the mongodDB -->> In future we will receive data from absence.io as well.
	tbl_bi = tbl_absence

	# files ready to be parsed: checked by the import_data module.
	exported_file = dict((el,0) for el in tbl_bi)
	
	#conn_cs = os.environ['conn_cs']

	conn_bi = os.environ['conn_bi']

	# allocation of db connection when runner program is executed. 
	@classmethod
	def dbconn(self,host):
		if(host == "absence"):
			#param.connection = self.conn_cs
			param.schema = "absence"
			param.newpath = param.root +'/' +param.start_date +'/'

		else:
			print("Invalid Host given : Please enter the details of the host mongoDB in param.py file ")



