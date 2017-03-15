from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
import etl_delta_load
import pandas as pd
import threading
import psycopg2
import os
import re


class Rerun():


	def main():

		try:

			conn_string = os.environ['conn_bi']
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()

			tbl = pd.read_sql("select distinct file_path, table_name, start_date, end_date from public.etl_status where schema_name not in ('sfdc') and status='fail'", conn)

			for table_name in tbl['table_name'].unique():
				if table_name in param.truncate_tbl:
					print("truncating table " +table_name)
					curs.execute(etl_delta_load.truncate_queries[table_name])
					conn.commit()

			for file_path in tbl['file_path'].unique():
				x = re.search(':00/(.+?).csv', file_path)
				y = re.search ('data/(.+?)/20', file_path)
				if x:
					table_name = x.group(1)
			    	if y:
			    		schema_name = y.group(1)
				if (os.stat(file_path).st_size > 4):
					file = open(file_path)
					curs.copy_expert(sql = """ COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ',' """ %(schema_name +'.' +table_name), file = file)
					print("delta load starts for:" +table_name)
					start_date = str(tbl['start_date'])
					new_start_date = (start_date.split()[1] + ' ' + start_date.split()[2]).replace(' Name:',' 00:00:00')
					end_date = str(tbl['end_date'])
					new_end_date = (end_date.split()[1] + ' ' + end_date.split()[2]).replace(' Name:',' 00:00:00')
					curs.execute(etl_delta_load.delta_query[table_name].replace(param.start_date, new_start_date).replace(param.end_date,new_end_date))
					curs.execute("update public.etl_status set status = %s where file_path = %s", ('pass', file_path))
					conn.commit()

		except Exception as e:
			print("Unable to access database, re-run error %s", str(e))
			conn.rollback()
			
		finally:
			curs.close()
			conn.close()


	if __name__ == "__main__":
		main()			
