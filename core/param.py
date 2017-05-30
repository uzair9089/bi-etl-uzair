
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
	#root = '/Users/sanjivupadhyaya/Desktop/'
	counter = 0 

	# should be always 1 - 2 hours
	start_date = datetime.datetime.now() - datetime.timedelta(hours = 2)
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
				,'pymt': os.environ['conn_pymt']
				,'intercom': os.environ['conn_intercom']
				,'bi': os.environ['conn_bi'] 
			}

	sources = ['core', 'nwsl', 'msg', 'comm', 'pymt', 'intercom']

	tbl_source = []

	tbl_source_truncate = []

	tbl_source_rename = []

	exported_file = {}

	#tbl_core= ['shifts','shift_plan_templates']
	tbl_core = ['appointment_services', 'appointment_resources', 'events', 'feedbacks', 
				'merchant_customers', 'shift_plan_templates', 'newsletters', 'resources', 'services', 
				'merchant_profiles', 'event_participants', 'appointment_series', 'shifts',
				'pdf_forms', 'customer_custom_attributes', 'appointment_occurrences',
				#'notification_channels', -- removed on 13th of may 'merchant_customer_tags', customers
				'newsletter_blacklists',
				'service_categories', 'closing_times', 'merchant_customer_custom_attributes', 'uberall_accounts']
	
	tbl_core_truncate = ['employees', 'merchant_permissions', 'merchant_key_accounts', 'merchant_accounts', 'merchant_roles']

	tbl_core_rename = {}

	tbl_nwsl = ['newsletters','newsletters_deprecated'] #remove the deprecated after the api moves to v2.

	tbl_nwsl_truncate = ['newsletter_customers_deprecated']

	tbl_nwsl_truncate = []

	tbl_nwsl_rename = {'newsletters': 'newsletters_nwsl'}

	tbl_msg = ['conversations', 'group_senders', 'merchant_senders', 'messages', 'participants']

	tbl_msg_truncate = ['conversation_senders']

	tbl_msg_rename = {}

	tbl_comm = ['sms', 'publications', 'emails']

	tbl_comm_truncate = ['merchants']

	tbl_comm_rename = {}

	tbl_pymt = []

	tbl_pymt_truncate = ['merchants', 'disputes', 'bank_accounts',  'stripe_events', 'charges', 'payments', 'charge_items', 'refunds'] # 'request_logs' was depricated

	tbl_pymt_rename = {'merchants': 'merchants_pymt'}

	tbl_intercom = ['companies', 'segments', 'contacts', 'users',
					 'conversations', 'conversation_parts']

	tbl_intercom_truncate = ['tags', 'admins']

	# if tables has been renamed while importing into our BI-DWH, then renamed_table has to be kept bzw., intercom			
	tbl_intercom_rename =  {'companies': 'companies_intercom', 'segments': 'segments_intercom', 'contacts': 'contacts_intercom','users': 'users_intercom', 
						'conversations':'conversations_intercom','conversation_parts': 'conversation_parts_intercom','tags': 'tags_intercom', 'admins': 'admins_intercom'}


	# complete list of tables to be extracted 
	#tbl_bi = tbl_core + tbl_core_truncate + tbl_msg + tbl_msg_truncate + tbl_comm + tbl_comm_truncate + tbl_intercom + tbl_intercom_truncate + tbl_nwsl + tbl_nwsl_truncate + tbl_pymt + tbl_pymt_truncate

	truncate_tbl = tbl_core_truncate + tbl_msg_truncate + tbl_comm_truncate + tbl_intercom_truncate + tbl_nwsl_truncate + tbl_pymt_truncate
	# files ready to be extracted: checked by the import_data module.


	table_hash = {'core':[{'tbl_source':tbl_core},{'tbl_source_truncate':tbl_core_truncate},{'tbl_source_rename':tbl_core_rename}], 
				  'nwsl':[{'tbl_source':tbl_nwsl},{'tbl_source_truncate':tbl_nwsl_truncate},{'tbl_source_rename':tbl_nwsl_rename}], 
				  'msg':[{'tbl_source':tbl_msg},{'tbl_source_truncate':tbl_msg_truncate},{'tbl_source_rename':tbl_msg_rename}], 
				  'comm':[{'tbl_source':tbl_comm},{'tbl_source_truncate':tbl_comm_truncate},{'tbl_source_rename':tbl_comm_rename}],
				  'pymt':[{'tbl_source':tbl_pymt},{'tbl_source_truncate':tbl_pymt_truncate},{'tbl_source_rename':tbl_pymt_rename}], 
				  'intercom':[{'tbl_source':tbl_intercom},{'tbl_source_truncate':tbl_intercom_truncate},{'tbl_source_rename':tbl_intercom_rename}]}



	# allocation of db connection when runner program is executed. 
	@classmethod
	def dbconn(self,host):
		if host in param.sources:
			param.connection = self.conn_hash[host]
			param.schema = host
			param.newpath = param.root +param.schema +'/' +param.start_date +'/'
		else:
			print("Invalid Host given : Please enter the details of the host in param.py file ")





