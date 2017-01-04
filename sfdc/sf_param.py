
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: Function: hold the parameters of ETL process including database connection, ETL run dates and directory      
"""

import time
import pprint
import datetime
import dateutil
import pandas as pd
from datetime import  date, timedelta
import os


class param:
	# 4 and - 1
	st_dt = datetime.datetime.utcnow() - datetime.timedelta(hours = 4)
	st_dt = st_dt.strftime('%Y-%m-%d %H:00:00')
	gmt_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(st_dt, "%Y-%m-%d %H:%M:%S"))))
	st_dt = gmt_dt.replace(' ','T')
	start_date =  str(st_dt) +'.000Z'

	end_date = datetime.datetime.utcnow() - datetime.timedelta(hours = 1)
	end_date = end_date.strftime('%Y-%m-%d %H:00:00')
	gmt_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(end_date, "%Y-%m-%d %H:%M:%S"))))
	end_date = gmt_dt.replace(' ','T')
	end_date = end_date+'.000Z'

	#filter data for delta loads
	rows = " where SystemModstamp >= " +start_date +" and SystemModstamp < " +end_date
	rows_leadhistory = " where createddate>=" +start_date +" and createddate <" +end_date
	#rows_lead_history=" "
	newpath = '/opt/etl/sfdc/sf_data/' +str(st_dt) +'/'

	user_name = os.environ['sf_username']
	password = os.environ['sf_password']
	token = os.environ['sf_token']
	passport = os.environ['sf_passport']

	# BI database
	conn_bi = os.environ['conn_bi']
	
	# files ready to be extracted
	tbl_bi = ['account','onb2__invoice__c', 'onb2__item__c', 'onb2__subscription__c', 'onb2__dunning__c'
	,'onb2__dunningdetail__c', 'lead', 'users', 'contract'
	,'recordtype', 'onb2__balance__c', 'contact', 'opportunity'
	,'onb2__dunningrun__c', 'asset', 'onb2__invoicelineitem__c', 'onb2__invoicerun__c','leadhistory']
	

	exported_file = dict((el,0) for el in tbl_bi)

	counter = 0

	exported_table = [] 

