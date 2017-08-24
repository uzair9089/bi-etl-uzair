
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
	root = '/opt/etl/recurly/data/'
	counter = 0 
	newpath = ""
	connection = ""
	start_date = str(date.today() - timedelta(1))
	end_date = str(date.today())

	row_count = 0 
	row_limit = 200
	loop_counter = 0
	skip_counter = 0

	# absence object to be imported
	tbl_recurly= ['subscriptions']
	counter = len(tbl_recurly)

	# history load if there are any
	history_objects = ['nothing']

	# used while loading the history data
	temp_objects = []

	# add the url for the new absence object
	url = {'subscriptions': "https://shore-dev.recurly.com/v2/subscriptions"
			}

	# filters are used for limiting and skipping the record fetched from the absence object
	filters ={
			  'subscriptions': "?per_page=200"
			  }
	
	# filters_new are used for daily load of data from the absence objects
	filters_new ={'subscriptions': "?per_page=200sort=updated_at&order=asc&begin_time=" + str(start_date)
				  }

	# headers are not to be changed after the implementation
	headers = {
		'Accept': 'application/xml',
		'X-Api-version': "2.5",
		'cache-control': "no-cache",
		'Content-Type': 'application/xml; charset=utf-8'
		}

	conn_bi = os.environ['conn_bi']
	# connection hash used to set up connections
	conn_hash = {
			'bi': conn_bi 
		}

	# insert the queries to be used if the table have to be truncated incase of missing modified date
	truncate_queries = {						
	}

	tbl_bi = tbl_recurly

	# convert the list into a dictionary and set the values to 0 in the beginning
	exported_file = dict((el,0) for el in tbl_bi)

	@classmethod
	def dbconn(self,host):
		if(host == "recurly"):
			param.schema = "recurly"
			param.newpath = param.root +'/' +param.start_date +'/'

		else:
			print("Invalid Host given : Please enter the details of the host mongoDB in param.py file ")



