from datetime import date, timedelta
import datetime
import os

class param:

	start_date = datetime.datetime.now() - datetime.timedelta(days = 1)
	start_date = start_date.strftime('%Y-%m-%d')

	end_date = datetime.datetime.now() - datetime.timedelta(days = 0)
	end_date = end_date.strftime('%Y-%m-%d')

	# The list holds the complete list of the ga_merchant_id
	merchant_list =  [127274158]  #85236967, 127274158, 114271445

	exclude_list = []

	conn_string = os.environ['conn_bi']