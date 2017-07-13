from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
from etl_delta_load import delta_query
import psycopg2
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ReasonsParser:

	def parser(self, collection_name):

		try:

			conn_string = param.conn_bi
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()

			# open the exported file
			file = open(param.newpath+collection_name,'r')

			for line in file:
				x = json.loads(line,strict=False) 
				keys_in_record = x.keys() 

				# declare the variables to be imported from the absence object
				if 'data' in keys_in_record:

					for data_lines in x["data"]:
						id = name = country = company = created = 'N/A' 
						modified = '1900-01-01'
						defaultVacationDays  =  0
						
						if '_id' in data_lines.keys():
							id = str(data_lines["_id"]).replace("'","")

					 	if 'modified' in data_lines.keys():
							modified = data_lines["modified"]

						if 'name' in data_lines.keys():
							name = data_lines["name"]

						if 'country' in data_lines.keys():
							country = str(data_lines["country"]).replace("'","")

						if 'company' in data_lines.keys():
							company = str(data_lines["company"]).replace("'","")

						if 'created' in data_lines.keys():
							created = data_lines["created"]

						if 'defaultVacationDays' in data_lines.keys():	
							defaultVacationDays = str(data_lines["defaultVacationDays"]).replace("'","")

						curs.execute("insert into absence.reasons(id, modified, name, country, company, created, defaultVacationDays) values ('{0}','{1}','{2}','{3}','{4}','{5}',{6})"
						.format(id, modified, name, country, company, created, defaultVacationDays))
						conn.commit()


			print("finished parsing data for: "+collection_name)

			print ("delta load starts ")
			curs.execute(delta_query['absences'])
			conn.commit()

		# log the exception into the etl_status if any error occurs
		except Exception as e:
			param.counter-1
			conn.rollback()
			curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
			.format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e).replace("'",""), 'fail'))
			conn.commit()
			conn.close()
			curs.close()

		finally:
			conn.close()
			curs.close()