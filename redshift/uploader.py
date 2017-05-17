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

class Uploader(Thread): 


	def __init__(self,full_file_path):
		Thread.__init__(self)
		self.file_name = full_file_path


	def run(self):

		try:

			os.environ['S3_USE_SIGV4'] = 'True'
			BUCKET_NAME = 'shore-bi-etl'
			AWS_ACCESS_KEY_ID = "AKIAIVBSMDRFXBB4YM6Q"
			AWS_SECRET_ACCESS_KEY="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"
			REGION_HOST = 's3.eu-central-1.amazonaws.com'
			conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
			                AWS_SECRET_ACCESS_KEY, host = REGION_HOST)
			#conn.create_bucket(BUCKET_NAME)
			bucket = conn.get_bucket(BUCKET_NAME)

			identifier = self.file_name

			file_exists_or_not = bucket.lookup(self.file_name)

			if bucket.lookup(self.file_name):
				file_exists_or_not.delete()

			k = Key(bucket)

			k.key = self.file_name

			k.set_contents_from_filename(self.file_name)
		except:
			print 'error while transferring data to the s3 bucket '+ self.file_name

# import_data function is called every minute by the runner program until ETL for all the tables are completed  
def upload_data_to_s3(key):
	for key, values in param.exported_file.iteritems():
		if(param.exported_file[key] == 1):
			print("Transferring data to the S3 bucket: "+ key)
			runner = Uploader( param.root + param.start_date + key + '.csv') # put the variable in the param file for the s3 bucket details
			param.exported_file[key] = 0
			param.redshift_counter = param.redshift_counter - 1
			runner.start()



