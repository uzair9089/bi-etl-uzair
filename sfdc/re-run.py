from sqlalchemy import create_engine
from threading import Thread, Lock
from sf_param import param
import etl_delta_load
import pandas as pd
import threading
import psycopg2
import os
import re


class Rerunsf():


	def main():

		try:

			conn_string = os.environ['conn_bi']
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()

			tbl = pd.read_sql("select distinct file_path, table_name from public.etl_status where schema_name in ('sfdc') and status='fail'", conn)

			for file_path in tbl['file_path'].unique():
				x = re.search(':00/(.+?).csv', file_path)
				y = re.search ('etl/(.+?)/sf_data', file_path)
				if x:
					table_name = x.group(1)
			    	if y:
			    		schema_name = y.group(1)
				if (os.stat(file_path).st_size > 4):
					file = open(file_path)
					curs.copy_expert(sql = """ COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ',' """ %(schema_name +'.' +table_name), file = file)
					print("delta load starts for:" +table_name)
					curs.execute(etl_delta_load.delta_query[table_name])
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
