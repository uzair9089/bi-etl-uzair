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

class UserParser:

	def parser(self, collection_name):

		try:

			conn_string = param.conn_bi
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()

			# truncate the table if present in the param file
			if collection_name in param.truncate_queries:
				curs.execute(param.truncate_queries[collection_name])
				curs.execute
				conn.commit()

			# open the exported file
			file = open(param.newpath+collection_name,'r')

			for line in file:
				x = json.loads(line,strict=False) 
				keys_in_record = x.keys() 

				if 'data' in keys_in_record:

					# declare the variables to be imported from the absence object
					for data_lines in x["data"]:
						id = company = email = status = language = first_login = first_name	= last_name = ics_link = location_id = roleId = activationDueDate = deletedDate ='N/A' 
						created = modified = '9999-01-01'
						
						if '_id' in data_lines.keys():
							id = str(data_lines["_id"]).replace("'","")

						if 'company' in data_lines.keys():
							company = data_lines["company"]

						if 'deletedDate' in data_lines.keys():
							deletedDate = data_lines["deletedDate"]

						if 'activationDueDate' in data_lines.keys():
							activationDueDate = data_lines["activationDueDate"]

						if 'roleId' in data_lines.keys():
							roleId = data_lines["roleId"].replace("'","")

						if 'email' in data_lines.keys():
							email = data_lines["email"].replace("'","")

						if 'status' in data_lines.keys(): 
							status = str(data_lines["status"]).replace("'","")

						if 'language' in data_lines.keys():
							language = str(data_lines["language"]).replace("'","")

						if 'firstLogin' in data_lines.keys():
							first_login = str(data_lines["firstLogin"]).replace("'","")

						if 'lastName' in data_lines.keys():
							last_name = str(data_lines["lastName"]).replace("'","")

						if 'icsLink' in data_lines.keys():
							ics_link = data_lines["icsLink"]

						if 'locationId' in data_lines.keys():
							location_id = str(data_lines["locationId"]).replace("'","")

						if 'created' in data_lines.keys():
							created = str(data_lines["created"])

						if 'modified' in data_lines.keys():
							modified =	str(data_lines["modified"])


						curs.execute("insert into absence.users(id, company, email, status, language, first_login, first_name, last_name, ics_link, location_id, created, modified, activation_due_date, roleId,	deletedDate) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')"
						.format(id, company, email, status, language, first_login, first_name, last_name, ics_link, location_id, created, modified, activationDueDate, roleId, deletedDate))

						conn.commit()

			print("finished parsing data for: " + collection_name)

			print ("delta load starts ")

			curs.execute(delta_query['users'])
			conn.commit()
		# log the error into the etl_status if any occurs
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