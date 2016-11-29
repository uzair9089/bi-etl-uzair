
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: Prepare fact and dimension table for the cube
"""

from datetime import date, timedelta
import pandas as pd
import datetime
import pprint
import time
import os



class config:

	start_date= datetime.datetime.now() - datetime.timedelta(hours=5)
	start_date= start_date.strftime('%Y-%m-%d %H:00:00')

	end_date= datetime.datetime.now() - datetime.timedelta(hours=2)
	end_date= end_date.strftime('%Y-%m-%d %H:00:00')		

	schema= "dmart"
	conn_bi = os.environ['conn_bi']
	sql_file_path = "/opt/etl/cubes/jobs/sql/"


