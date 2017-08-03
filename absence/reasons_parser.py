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
						id = name = company = allowanceTypeId = deleted = reducesDays = isPublic = 'N/A' 
						modified = '1900-01-01'
						defaultVacationDays  =  0.0
						
						if '_id' in data_lines.keys():
							id = str(data_lines["_id"]).replace("'","")

						if 'modified' in data_lines.keys():
							modified = data_lines["modified"]

						if 'name' in data_lines.keys():
							name = data_lines["name"].replace("'","")

						if 'allowanceTypeId' in data_lines.keys():
							allowanceTypeId = str(data_lines["allowanceTypeId"]).replace("'","")

						if 'company' in data_lines.keys():
							company = str(data_lines["company"]).replace("'","")

						if 'deleted' in data_lines.keys():
							deleted = data_lines["deleted"]

						if 'reducesDays' in data_lines.keys():
							reducesDays = data_lines["reducesDays"]

						if 'isPublic' in data_lines.keys():
							isPublic = data_lines["isPublic"]

						if 'defaultVacationDays' in data_lines.keys():	
							defaultVacationDays = str(data_lines["defaultVacationDays"]).replace("'","")

						curs.execute("insert into absence.reasons(id, modified, name, allowanceTypeId, company, deleted, reducesDays, isPublic, defaultVacationDays) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8})"
						.format(id, modified, name, allowanceTypeId, company, deleted, reducesDays, isPublic, defaultVacationDays))
						conn.commit()


			print("finished parsing data for: "+collection_name)

			print ("delta load starts ")
			curs.execute(delta_query['reasons'])
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