from datetime import date, timedelta
import datetime
import os

class param:

	# 1 and 0
	start_date = datetime.datetime.now() - datetime.timedelta(days = 40)
	start_date = start_date.strftime('%Y-%m-%d')

	end_date = datetime.datetime.now() - datetime.timedelta(days = 10)
	end_date = end_date.strftime('%Y-%m-%d')

	# The list holds the complete list of the ga_merchant_id
	merchant_list =  [85236967]
	#, 141301709, 141313101, 141306904, 151106256,  127274158]

	exclude_list = []

	conn_string = os.environ['conn_bi']