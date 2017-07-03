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

class AbsencesParser:

	def parser(self, collection_name):

		print "parsing for the "+ collection_name

		try:

			conn_string = param.conn_bi
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()

			file = open(param.newpath+collection_name,'r')

			for line in file:
				x = json.loads(line,strict=False) 
				keys_in_record = x.keys() 
				print keys_in_record

				if 'data' in keys_in_record:

					for data_lines in x["data"]:
						id =  modified = start_date = end_date = company = created = reason_id = assigned_to_id = approver_id = status = deny_reason = 'N/A' 
						days_count  =  0
						
						if '_id' in data_lines.keys():
							id = str(data_lines["_id"]).replace("'","")
					 		print id

					 	if 'modified' in data_lines.keys():
							modified = data_lines["modified"]
							print modified

						if 'start' in data_lines.keys():
							start_date = data_lines["start"]
							print start_date

						if 'end' in data_lines.keys():
							end_date = str(data_lines["end"]).replace("'","")
							print end_date

						if 'company' in data_lines.keys():
							company = str(data_lines["company"]).replace("'","")
							print company

						if 'created' in data_lines.keys():
							created = data_lines["created"]
							print created

						if 'reasonId' in data_lines.keys():	
							reason_id = str(data_lines["reasonId"]).replace("'","")
							print reason_id

						if 'assignedToId' in data_lines.keys():
							assigned_to_id = str(data_lines["assignedToId"]).replace("'","")
							print assigned_to_id

						if 'approverId' in data_lines.keys():
							approver_id = str(data_lines["approverId"]).replace("'","")
							print approver_id

						if 'daysCount' in data_lines.keys():
							days_count = str(data_lines["daysCount"]).replace("'","")
							print days_count

						curs.execute("insert into absence.absences(id,  modified, start_date, end_date, company, created, reason_id, assigned_to_id, approver_id, days_count) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',{9})"
						.format(id,  modified, start_date, end_date, company, created, reason_id, assigned_to_id, approver_id, days_count))
						conn.commit()


			print("finished parsing data for: "+collection_name)

			print ("delta load starts ")
			curs.execute(delta_query['absences'])
			conn.commit()

		except Exception as e:
			param.counter-1
			print ("exception")
			print e
			conn.rollback()
			curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
			.format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e).replace("'",""), 'fail'))
			conn.commit()
			conn.close()
			curs.close()

		finally:
			conn.close()
			curs.close()