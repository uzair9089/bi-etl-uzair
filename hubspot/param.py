
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
	root = '/Users/sanjivupadhyaya/Desktop/mars1/etl/hubspot/data'
	#root = '/opt/etl/absence/data'
	counter = 0
	newpath = ""
	connection = ""
	previous_date = str(date.today() - timedelta(2)) # day before yesterday
	start_date = str(date.today() - timedelta(1)) # yesterday
	end_date = str(date.today()) # today
	pattern = '%Y-%m-%d'
	#converting the datetime to epoch for hubspot data extraction
	previous_date = int(time.mktime(time.strptime(previous_date, pattern)))
	start_date = int(time.mktime(time.strptime(start_date, pattern)))
	end_date = int(time.mktime(time.strptime(end_date, pattern)))


	time_offset = 0

	vid_offset = 0

	tbl_hubspot = ['contacts']

	history_objects = ['contacts']

	temp_objects = []

	# put the hapi key into the environment variables
	url = {'contacts': "https://api.hubapi.com/contacts/v1/lists/recently_updated/contacts/recent"}

	new_url = ""

	recent_querystring = {"hapikey":os.environ['hubspot'], "count":"1000000"}

	querystring = {"hapikey":os.environ['hubspot'], "count":"1000000","vidOffset":vid_offset,"timeOffset":time_offset}

	#querystring =	{"hapikey":os.environ['hubspot'],"vidOffset":"267292","timeOffset":"1428077720267","count":"1000000"}

	# move the token to the environment variable somehow
	headers = {
		'cache-control': "no-cache",
		'postman-token': "c20dbdb9-2cdc-033f-4484-5f4b4f8bb125"
	    }


	# dictionary for storing truncate queries for tables without the date attributes.
	truncate_queries = {
						# example schema--> change it to appropriate table name in future when required
						'contacts': "truncate table hubspot.contacts;"
	}

	# complete list of collections to be extracted from the mongodDB -->> In future we will receive data from absence.io as well.
	tbl_bi = tbl_hubspot

	# files ready to be parsed: checked by the import_data module.
	exported_file = dict((el,0) for el in tbl_bi)
	
	#conn_cs = os.environ['conn_cs']e

	conn_bi = os.environ['conn_bi']

	# allocation of db connection when runner program is executed. 
	@classmethod
	def dbconn(self,host):
		if(host == "hubspot"):
			#param.connection = self.conn_cs
			param.schema = "hubspot"
			param.newpath = param.root +'/' +str(param.start_date) +'/'

		else:
			print("Invalid Host given : Please enter the details of the host mongoDB in param.py file ")



