from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
import etl_delta_load
import psycopg2
import os
import json
import sys


reload(sys)

sys.setdefaultencoding('utf8')

class CompanyParser:

	def parser(self, collection_name):

		try:

			conn_string = param.conn_bi
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()

			file = open(param.newpath+collection_name,'r')

			for line in file:
				x = json.loads(line,strict=False) 
				keys_in_record = x.keys() 
				#print keys_in_record

				if 'data' in keys_in_record:

					for data_lines in x["data"]:
						id =  modified = created = name = email = region = country = first_bill_date = company_size = suspended =  test_expired = pricing_type = billing_interval = payment_type = is_billed = 'N/A'
						team_count = user_billable_count = yearly_revenue = activity_index = days_active = price_flat = user_count = user_active_count = user_deleted_count =  0
						
						id = str(data_lines["id"]).replace("'","")
					 	#print id

					 	if 'modified' in data_lines.keys():
							modified = data_lines["modified"]
							#print modified

						if 'created' in data_lines.keys():
							created = data_lines["created"]
							#print created

						if 'name' in data_lines.keys():	
							name = str(data_lines["name"]).replace("'","")
							#print name

						if 'email' in data_lines.keys():
							email = str(data_lines["email"]).replace("'","")
							#print email

						if 'region' in data_lines.keys():
							region = str(data_lines["region"]).replace("'","")
							#print region

						if 'name' in data_lines.keys():
							country = str(data_lines["country"]).replace("'","")
							#print country

						if 'firstBilldate' in data_lines.keys():
							first_bill_date = data_lines["firstBilldate"]
							#print first_bill_date
							#print ("before size")

						if 'companySize' in data_lines.keys():
							company_size =  data_lines["companySize"]["value"]
							#print company_size
						#print("after size")

						if 'customSettings' in data_lines.keys():
							if 'suspended' in data_lines["customSettings"]:
								suspended =  str(data_lines["customSettings"]["suspended"]).replace("'","")
								#print suspended

						if 'stats' in data_lines.keys():
							if 'teamCount' in data_lines["stats"]:
								teamCount = str( data_lines["stats"]["teamCount"]).replace("'","")
								#print team_count

						if 'stats' in data_lines.keys():
							if 'userBillableCount' in data_lines["stats"]:
								user_billable_count =  data_lines["stats"]["userBillableCount"]
								#print user_billable_count

						if 'stats' in data_lines.keys():
							if 'yearlyRevenue' in data_lines["stats"]:
								yearly_revenue =  data_lines["stats"]["yearlyRevenue"]
								#print yearly_revenue

						if 'stats' in data_lines.keys():
							if 'activityIndex' in data_lines["stats"]:
								activity_index =  data_lines["stats"]["activityIndex"]
								#print activity_index

						if 'stats' in data_lines.keys():
							if 'userCount' in data_lines["stats"]:
								user_count =  data_lines["stats"]["userCount"]
								#print user_count

						if 'stats' in data_lines.keys():
							if 'userActiveCount' in data_lines["stats"]:
								user_active_count =  data_lines["stats"]["userActiveCount"]
								#print user_active_count

						if 'stats' in data_lines.keys():
							if 'userDeletedCount' in data_lines["stats"]:
								user_deleted_count =  data_lines["stats"]["userDeletedCount"]
								#print user_deleted_count

						if 'stats' in data_lines.keys():
							if 'daysActive' in data_lines["stats"]:
								days_active =  data_lines["stats"]["daysActive"]
								#print days_active

						if 'priceFlat' in data_lines.keys():
							price_flat = data_lines["priceFlat"]
							#print price_flat 

						if 'testPeriodExpired' in data_lines.keys():	
							test_expired = str(data_lines["testPeriodExpired"]).replace("'","")
							#print test_expired

						#print ("here")
						if 'isBilled' in data_lines.keys():
							is_billed = str(data_lines["isBilled"]).replace("'","")
							#print is_billed
						#print("out")
						if 'isTest' in data_lines.keys():
							billing_interval = str(data_lines["isTest"]).replace("'","")
							#print billing_interval

						if 'active' in data_lines.keys():
							is_active = str(data_lines["active"]).replace("'","")
							#print is_active

						if 'isSuspended' in data_lines.keys():	
							is_suspended = str(data_lines["isSuspended"]).replace("'","")
							#print is_suspended

						if 'pricePerUser' in data_lines.keys():
							price_per_user = str(data_lines["pricePerUser"]).replace("'","")
							#print price_per_user

						if 'pricingType' in data_lines.keys():
							pricing_type = str(data_lines["pricingType"]).replace("'","")
							#print pricing_type

						if 'billingIntervall' in data_lines.keys():
							billing_interval = str(data_lines["billingIntervall"]).replace("'","")
							#print billing_interval

						if 'payment_type' in data_lines.keys():
							payment_type = str(data_lines["paymentType"]).replace("'","")
							#print payment_type

						#print ("insert into absence.company(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type,is_billed, user_count, user_active_count, user_deleted_count) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',{10},{11},{12},{13},{14},{15},'{16}','{17}','{18}','{19}','{20}',{21},{22},{23})"
						#.format(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type, is_billed,user_count, user_active_count, user_deleted_count))
					

						#print ("here")
						curs.execute("insert into absence.company(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type, is_billed,user_count, user_active_count, user_deleted_count) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',{10},{11},{12},{13},{14},{15},'{16}','{17}','{18}','{19}','{20}',{21},{22},{23})"
						.format(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type,is_billed,user_count, user_active_count, user_deleted_count))
						conn.commit()
						#print ("here after commit")

			#curs.execute(etl_delta_load.delta_query[collection_name[:-5]]).replace("'","")
			#conn.commit()

			print("finished parsing data for: "+collection_name)

		except Exception as e:
			param.counter-1
			print ("exception")
			conn.rollback()
			curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
			.format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e), 'fail'))
			conn.commit()
			conn.close()
			curs.close()

		finally:
			conn.close()
			curs.close()