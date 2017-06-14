
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
	#root = '/Users/sanjivupadhyaya/Desktop/repo/etl/absence/data'
	root = '/opt/etl/absence/data'
	counter = 0 
	newpath = ""
	connection = ""
	start_date = str(date.today() - timedelta(1))
	end_date = str(date.today())

	row_count = 0 
	row_limit = 500
	loop_counter = 0
	skip_counter = 0

	tbl_absence= ['company', 'invoices','users']

	history_objects = ['Mention History Table from Above if required']

	temp_objects = []

	url = {'company': "https://app.absence.io/api/v2/bi/companies"
		   ,'invoices': "https://app.absence.io/api/v2/bi/invoices"
		   ,'users': "https://app.absence.io/api/v2/bi/users"
			}

	filters ={
			  'company': "{\n\t\n\t\"limit\":500,"+"\n\t\"skip\":"
			  ,'invoices': "{\n\t\"limit\": 1000\n\n}"
			  ,'users':"{\n\t\n\t\"limit\":500,"+"\n\t\"skip\":"}
	

	filters_new ={'company': "{\n\t\"limit\": 1000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n }\n}"
		  ,'invoices': "{\n\t\"limit\": 1000\n\n}"
		  ,'users': "{\n\t\"limit\": 1000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n }\n}"}


	headers = {
	    'x-vacationtoken': os.environ['x_vacationtoken'],
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': os.environ['postman_token']
	    }


	# dictionary for storing truncate queries for tables without the date attributes.
	truncate_queries = {
						# example schema--> change it to appropriate table name in future when required
						'invoices': "truncate table absence.invoices;"
						,'users': "truncate table absence.users;"
						,'example2': "truncate table cs.eample2;"
						
	}

	tbl_bi = tbl_absence

	# files ready to be parsed: checked by the import_data module.
	exported_file = dict((el,0) for el in tbl_bi)

	conn_bi = os.environ['conn_bi']

	# allocation of db connection when runner program is executed. 
	@classmethod
	def dbconn(self,host):
		if(host == "absence"):
			param.schema = "absence"
			param.newpath = param.root +'/' +param.start_date +'/'

		else:
			print("Invalid Host given : Please enter the details of the host mongoDB in param.py file ")



