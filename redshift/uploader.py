"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: upload file to the s3 server and then start the import
"""

from sqlalchemy import create_engine
from threading import Thread, Lock
from boto.s3.key import Key
from param import param
import etl_delta_load
import pandas as pd
import threading
import psycopg2
import boto
import os
from importer import Importer
import importer

class Uploader(Thread): 


	def __init__(self, full_file_path, table_name):
		Thread.__init__(self)
		self.file_name = full_file_path
		self.table_name = table_name


	def run(self):

		try:

			#print self.file_name

			os.environ['S3_USE_SIGV4'] = 'True'
			BUCKET_NAME = param.BUCKET_NAME 
			AWS_ACCESS_KEY_ID = param.AWS_ACCESS_KEY_ID 
			AWS_SECRET_ACCESS_KEY= param.AWS_SECRET_ACCESS_KEY 
			REGION_HOST = param.REGION_HOST 
			conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
			                AWS_SECRET_ACCESS_KEY, host = REGION_HOST)

			bucket = conn.get_bucket(BUCKET_NAME)

			identifier = self.file_name

			file_exists_or_not = bucket.lookup(self.file_name)

			if bucket.lookup(self.file_name):
				file_exists_or_not.delete()
				print 'file does not exists so needed to add'

			k = Key(bucket)

			k.key = self.file_name

			k.set_contents_from_filename(self.file_name)

			# call the import function here 

			#print 'Importing into the redhisft begins here'
			# To do Import into the redhshift from this block of the code

			#print self.table_name + " and " + param.full_path 
			runner = Importer(self.table_name, param.full_path+self.table_name+'.csv')
			#param.counter = param.counter - 1
			runner.start()

		except:
			print 'error while transferring data to the s3 bucket '+ self.file_name

# import_data function is called every minute by the runner program until ETL for all the tables are completed  
def upload_data_to_s3():
	for key, values in param.exported_file.iteritems():
		if(param.exported_file[key] == 1):
			#print (param.root + param.schema + '/' +  param.start_date  +  '/' + key + '.csv' , key) 
			runner = Uploader( param.root + param.schema + '/' +  param.start_date  +  '/' + key + '.csv' , key) # put the variable in the param file for the s3 bucket details 
			param.exported_file[key] = 0
			param.redshift_counter = param.redshift_counter - 1
			#print param.redshift_counter
			runner.start()




