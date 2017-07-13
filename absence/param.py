
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
	root = '/opt/etl/absence/data/'
	counter = 0 
	newpath = ""
	connection = ""
	start_date = str(date.today() - timedelta(1))
	end_date = str(date.today())

	row_count = 0 
	row_limit = 500
	loop_counter = 0
	skip_counter = 10

	# absence object to be imported
	tbl_absence= ['company', 'invoices','users', 'absences', 'reasons']

	# history load if there are any
	history_objects = ['Nothing here']

	# used while loading the history data
	temp_objects = []

	# add the url for the new absence object
	url = {'company': "https://app.absence.io/api/v2/bi/companies"
		   ,'invoices': "https://app.absence.io/api/v2/bi/invoices"
		   ,'users': "https://app.absence.io/api/v2/bi/users"
		   ,'absences': "https://app.absence.io/api/v2/bi/absences"
		   ,'reasons': "https://app.absence.io/api/v2/bi/reasons"
			}

	# filters are used for limiting and skipping the record fetched from the absence object
	filters ={
			  'company': "{\n\t\n\t\"limit\":500,"+"\n\t\"skip\":"
			  ,'invoices': "{\n\t\"limit\": 1000\n\n}"
			  ,'users':"{\n\t\n\t\"limit\":500,"+"\n\t\"skip\":"
			  ,'absences': "{\n\t\n\t\"limit\":500,"+"\n\t\"skip\":" 
			  ,'reasons': "{\n\t\n\t\"limit\":500,"+"\n\t\"skip\":" 
			  }
	
	# filters_new are used for daily load of data from the absence objects
	filters_new ={'company': "{\n\t\"limit\": 1000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n }\n}"
		  ,'invoices': "{\n\t\"limit\": 1000\n\n}"
		  ,'users': "{\n\t\"limit\": 1000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n }\n}"
	   	  ,'absences': "{\n\t\"limit\": 1000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n \t\t\t},\n \"sortBy\": {\"company\": 1}\n}"
	   	  ,'reasons': "{\n\t\"limit\": 1000,\n\t\"filter\": {\n  \t\"modified\": {\n\t\"$gte\": \"" + str(start_date) + "\",\n\t\"$lt\": \"" + str(end_date) + "\"\n   }\n \t\t\t},\n \"sortBy\": {\"company\": 1}\n}"
		  }

	# headers are not to be changed after the implementation
	headers = {
	    'x-vacationtoken': os.environ['x_vacationtoken'],
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': os.environ['postman_token']
	    }

	# insert the queries to be used if the table have to be truncated incase of missing modified date
	truncate_queries = {
						'invoices': "truncate table absence.invoices;"
						,'users': "truncate table absence.users;"
						,'example2': "truncate table cs.eample2;"
						,'absences': "select 1;"
						,'reasons': "select 1;"
						
	}

	tbl_bi = tbl_absence

	# convert the list into a dictionary and set the values to 0 in the beginning
	exported_file = dict((el,0) for el in tbl_bi)

	conn_bi = os.environ['conn_bi']

	@classmethod
	def dbconn(self,host):
		if(host == "absence"):
			param.schema = "absence"
			param.newpath = param.root +'/' +param.start_date +'/'

		else:
			print("Invalid Host given : Please enter the details of the host mongoDB in param.py file ")



