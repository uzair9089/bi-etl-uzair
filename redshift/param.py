
"""
Author: Sanjiv Upadhayaya
Date: 2016-10-03
Function: hold the parameters of ETL process including database connection, ETL run dates and directory
"""

from datetime import date, timedelta
import pandas as pd
import datetime
import pprint
import time
import os


class param:		

	connection = ""
	schema = ""
	newpath = ""

	root = '/opt/etl/core/data/'
	counter = redshift_counter = 0

	BUCKET_NAME = os.environ['s3_bucket']
	AWS_ACCESS_KEY_ID = os.environ['aws_access_key_id']
	AWS_SECRET_ACCESS_KEY= os.environ['aws_secret_access_key']
	REGION_HOST = os.environ['region_host']

	# should be always 24 hours
	start_date = datetime.datetime.now() - datetime.timedelta(hours = 25)
	start_date = start_date.strftime('%Y-%m-%d %H:00:00')

	end_date = datetime.datetime.now() - datetime.timedelta(hours = 1)
	end_date = end_date.strftime('%Y-%m-%d %H:00:00')

	reset_time = end_date[11:13]

	reset_value = '00'
	
	reset_start_date = datetime.datetime.now() - datetime.timedelta(hours = 241)
	reset_start_date = reset_start_date.strftime('%Y-%m-%d %H:00:00')

	reset_end_date =  datetime.datetime.now() - datetime.timedelta(hours = 1)
	reset_end_date = reset_end_date.strftime('%Y-%m-%d %H:00:00')


	# database connections for source and destination
	conn_hash = {
				'nwsl': os.environ['conn_nwsl']
				,'core': os.environ['conn_core']
				,'msg': os.environ['conn_msg']
				,'comm': os.environ['conn_comm']
				,'pymt': os.environ['conn_bi']
				,'intercom': os.environ['conn_intercom']
				,'bi': os.environ['conn_bi'] 
				,'star': os.environ['conn_bi']
				,'pentaho': os.environ['conn_bi']
				,'redshift': os.environ['conn_redshift']
			}

	sources = ['core', 'nwsl', 'msg', 'comm', 'pymt', 'intercom', 'star' ,'pentaho']

	tbl_source = []

	tbl_source_truncate = []

	tbl_source_rename = []

	exported_file = {}

	tbl_core= []

	tbl_core_truncate = []

	tbl_core_rename = {}

	tbl_star = [
				# views
				#'employees', 'feedbacks', 'merchant_customers', 'merchant_key_account_feature_toggles', 'merchant_key_accounts', 'pages_intercom' ]



	tbl_star_rename = {}

	tbl_star_truncate = [
						# tables
						'salesforce_accounts'
						]

	tbl_pentaho = []

	tbl_pentaho_rename = {}

	tbl_pentaho_truncate = [
	
				# growth cube
				'list_date_02',
				'list_sfdc_accounts',
				'list_city',
				'list_industry',
				'list_subscription_channel',
				'list_subscription_status',
				'list_subscription_start_date',
				'list_subscription_end_date',
				'fact_growth_general',
				'list_owner',

				# key account 
				'list_created_by_merchant',
				'list_state',
				'given_feedbacks',
				'list_date',
				'list_hour',
				'list_key_accounts_account',
				'list_widget_in_date',
				'fact_key_accounts_appointments']


	tbl_nwsl = []

	tbl_nwsl_truncate = []

	tbl_nwsl_rename = {}

	tbl_msg = []

	tbl_msg_truncate = []

	tbl_msg_rename = {}

	tbl_comm = []

	tbl_comm_truncate = []

	tbl_comm_rename = {}

	tbl_pymt = []

	tbl_pymt_truncate = []

	tbl_pymt_rename = {}

	tbl_intercom = []

	tbl_intercom_truncate = []
	
	tbl_intercom_rename =  {}

	truncate_tbl = tbl_core_truncate + tbl_msg_truncate + tbl_comm_truncate + tbl_intercom_truncate + tbl_nwsl_truncate + tbl_pymt_truncate

	table_hash = {'core':[{'tbl_source':tbl_core},{'tbl_source_truncate':tbl_core_truncate},{'tbl_source_rename':tbl_core_rename}], 
				  'nwsl':[{'tbl_source':tbl_nwsl},{'tbl_source_truncate':tbl_nwsl_truncate},{'tbl_source_rename':tbl_nwsl_rename}], 
				  'msg':[{'tbl_source':tbl_msg},{'tbl_source_truncate':tbl_msg_truncate},{'tbl_source_rename':tbl_msg_rename}], 
				  'comm':[{'tbl_source':tbl_comm},{'tbl_source_truncate':tbl_comm_truncate},{'tbl_source_rename':tbl_comm_rename}],
				  'pymt':[{'tbl_source':tbl_pymt},{'tbl_source_truncate':tbl_pymt_truncate},{'tbl_source_rename':tbl_pymt_rename}], 
				  'intercom':[{'tbl_source':tbl_intercom},{'tbl_source_truncate':tbl_intercom_truncate},{'tbl_source_rename':tbl_intercom_rename}],
				  'star':[{'tbl_source':tbl_star},{'tbl_source_truncate':tbl_star_truncate},{'tbl_source_rename':tbl_star_rename}],
				   'pentaho':[{'tbl_source':tbl_pentaho},{'tbl_source_truncate':tbl_pentaho_truncate},{'tbl_source_rename':tbl_pentaho_rename}]}



	# allocation of db connection when runner program is executed.
	@classmethod
	def dbconn(self,host):
		if host in param.sources:
			param.connection = self.conn_hash[host]
			param.schema = host
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'
			param.full_path = param.root + param.schema + '/' +  param.start_date  +  '/'
		else:
			print("Invalid Host given : Please enter the details of the host in param.py file ")





