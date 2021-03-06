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
			os.environ['S3_USE_SIGV4'] = 'True'
			BUCKET_NAME = param.BUCKET_NAME 
			AWS_ACCESS_KEY_ID = param.AWS_ACCESS_KEY_ID 
			AWS_SECRET_ACCESS_KEY= param.AWS_SECRET_ACCESS_KEY 
			REGION_HOST = param.REGION_HOST 
			conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
			                AWS_SECRET_ACCESS_KEY, host = REGION_HOST)

			print("debugging uploader 1")
			bucket = conn.get_bucket(BUCKET_NAME)

			print("debugging uploader 2")

			identifier = self.file_name

			file_exists_or_not = bucket.lookup(self.file_name)

			if bucket.lookup(self.file_name):
				file_exists_or_not.delete()

			k = Key(bucket)

			k.key = self.file_name

			k.set_contents_from_filename(self.file_name)

			print("debugging uploader 3")
			runner = Importer(self.table_name, param.full_path+self.table_name+'.csv')

			runner.start()

			print("debugging uploader 4")
		except:
			print 'error while transferring data to the s3 bucket '+ self.file_name

# import_data function is called every minute by the runner program until ETL for all the tables are completed  
def upload_data_to_s3():
	for key, values in param.exported_file.iteritems():
		if(param.exported_file[key] == 1):
			runner = Uploader( param.root + param.schema + '/' +  param.start_date  +  '/' + key + '.csv' , key) 
			param.exported_file[key] = 0
			param.redshift_counter = param.redshift_counter - 1
			runner.start()




