
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
	counter = 0 # counter for imported tables. Used to stop the ETL process.

	# should be always 1 - 2 hours
	# to run every hour change it to 2 and 1 both are negatives
	start_date = datetime.datetime.now() - datetime.timedelta(hours = 34)
	start_date = start_date.strftime('%Y-%m-%d %H:00:00')

	end_date = datetime.datetime.now() - datetime.timedelta(hours = 10)
	end_date = end_date.strftime('%Y-%m-%d %H:00:00')

	# database connections for source and destination
	conn_nwsl = os.environ['conn_nwsl']
	conn_core = os.environ['conn_core']
	conn_msg = os.environ['conn_msg']
	conn_comm = os.environ['conn_comm']
	conn_pymt = os.environ['conn_pymt']
	conn_intercom = os.environ['conn_intercom']
	conn_bi = os.environ['conn_bi']

	#tbl_core= ['shifts','shift_plan_templates']
	tbl_core = ['appointment_services', 'appointment_resources', 'customers', 'merchant_accounts', 'events', 'feedbacks', 
				'merchant_customers', 'shift_plan_templates', 'newsletters', 'resources', 'services', 
				'merchant_profiles', 'event_participants', 'appointment_series', 'shifts',
				'pdf_forms', 'merchant_customer_tags', 'customer_custom_attributes', 
				#'notification_channels', 
				'newsletter_blacklists',
				'service_categories', 'closing_times', 'merchant_customer_custom_attributes', 'uberall_accounts']

	tbl_nwsl = ['newsletters']

	tbl_msg = ['conversations', 'group_senders', 'merchant_senders', 'messages', 'participants']

	tbl_comm = ['sms', 'publications', 'emails']

	tbl_pymt = ['disputes', 'bank_accounts', 'request_logs', 'stripe_events', 'charges']

	tbl_intercom = ['companies', 'segments', 'contacts',
					'users', 'conversations', 'conversation_parts']


	# tables which are truncated and has no date attributes.
	tbl_except= ['newsletter_customers', 'employees', 'merchant_permissions', 'conversation_senders', 'newsletters_nwsl', 'merchants', 'merchant_key_accounts',
				'disputes', 'bank_accounts', 'request_logs', 'stripe_events', 'charges', 'merchants_pymt', 'tags_intercom', 'admins_intercom']

	# if tables has been renamed while importing into our BI-DWH, then renamed_table has to be kept bzw., intercom			
	tbl_intercom_rt =  ['companies_intercom', 'segments_intercom', 'contacts_intercom',
					'users_intercom', 'conversations_intercom', 'conversation_parts_intercom']

	# tables which are truncated and has no date attributes.
	truncate_tbl = ['newsletter_customers', 'employees', 'merchant_permissions', 'merchant_key_accounts', 'conversation_senders', 'merchants', 'disputes', 
					'bank_accounts', 'request_logs', 'stripe_events', 'charges', 'merchants_pymt', 'admins_intercom', 'tags_intercom']

	# dictionary for storing truncate queries for tables without the date attributes.
	truncate_queries = {
						# newsletters
						'newsletter_customers': "truncate table nwsl.newsletter_customers;"
						# core
						,'employees': "truncate table core.employees;"
						,'merchant_key_accounts':"truncate table core.merchant_key_accounts;"
						,'merchant_permissions':"truncate table core.merchant_permissions;"
						# messages
						,'conversation_senders': "truncate table msg.conversation_senders;"
						# communication
						,'merchants': "truncate table comm.merchants;"
						# payment
						,'merchants_pymt': "truncate table pymt.merchants_pymt;"
						,'disputes': "truncate table pymt.disputes;"
						,'bank_accounts': "truncate table pymt.bank_accounts;"
						,'request_logs': "truncate table pymt.request_logs;"
						,'stripe_events': "truncate table pymt.stripe_events;"
						,'charges': "truncate table pymt.charges;"
						# intercom
						,'tags_intercom': "truncate table intercom.tags_intercom;"
						,'admins_intercom': "truncate table intercom.admins_intercom;"
	}


	# complete list of tables to be extracted 
	tbl_bi = tbl_core + tbl_msg + tbl_comm + tbl_intercom_rt + tbl_except

	# files ready to be extracted: checked by the import_data module.
	exported_file = dict((el,0) for el in tbl_bi)


	# allocation of db connection when runner program is executed. 
	@classmethod
	def dbconn(self,host):
		if(host == "nwsl"):
			param.connection = self.conn_nwsl
			param.schema = "nwsl"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'

		elif(host == "msg"):
			param.connection = self.conn_msg
			param.schema = "msg"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'

		elif(host == "core"):
			param.connection = self.conn_core
			param.schema = "core"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'

		elif(host == "comm"):
			param.connection = self.conn_comm
			param.schema = "comm"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'

		elif(host == "pymt"):
			param.connection = self.conn_pymt
			param.schema = "pymt"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'
		
		elif(host == "intercom"):
			param.connection = self.conn_intercom
			param.schema = "intercom"
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'


		elif(host == "bi"):
			param.connection = self.conn_bi

		else:
			print("Invalid Host given : Please enter the details of the host in param.py file ")



