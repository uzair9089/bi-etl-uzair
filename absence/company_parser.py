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
				print keys_in_record
				id =  modified = created = name = email = region = country = first_bill_date = company_size = suspended = team_count = user_billable_count = yearly_revenue = activity_index = days_active = price_flat =  test_expired = pricing_type = billing_interval = payment_type = ''
				if 'data' in keys_in_record:
					id = str(x["data"][0]["id"])
					print id
					modified = x["data"][0]["modified"]
					print modified
					created = x["data"][0]["created"]
					print created
					name = str(x["data"][0]["name"])
					print name
					email = str(x["data"][0]["email"])
					print email
					region = str(x["data"][0]["region"])
					print region
					country = str(x["data"][0]["name"])
					print country
					first_bill_date = x["data"][0]["firstBilldate"]
					print first_bill_date
					company_size =  str(x["data"][0]["companySize"]["value"])
					print company_size
					suspended =  str(x["data"][0]["customSettings"]["suspended"])
					print suspended
					team_count = str( x["data"][0]["stats"]["teamCount"])
					print team_count
					user_billable_count =  x["data"][0]["stats"]["userBillableCount"]
					print user_billable_count
					yearly_revenue =  str(x["data"][0]["stats"]["yearlyRevenue"])
					print yearly_revenue
					activity_index =  str(x["data"][0]["stats"]["activityIndex"])
					print activity_index
					days_active =  x["data"][0]["stats"]["daysActive"]
					print days_active
					price_flat = str(x["data"][0]["priceFlat"])
					print price_flat 
					test_expired = str(x["data"][0]["testPeriodExpired"])
					print test_expired
					pricing_type = str(x["data"][0]["isBilled"])
					print pricing_type
					billing_interval = str(x["data"][0]["isTest"])
					print billing_interval
					is_active = str(x["data"][0]["active"])
					print is_active
					is_suspended = str(x["data"][0]["isSuspended"])
					print is_suspended
					price_per_user = str(x["data"][0]["pricePerUser"])
					print price_per_user
					pricing_type = str(x["data"][0]["pricingType"])
					print pricing_type
					billing_interval = str(x["data"][0]["billingIntervall"])
					print billing_interval
					payment_type = str(x["data"][0]["paymentType"])
					print payment_type

					print ("insert into absence.company(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}')"
					.format(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type))
					

					print ("here")
					curs.execute ("insert into absence.company(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}')"
					.format(id,  modified, created, name, email, region, country, first_bill_date, company_size, suspended, team_count, user_billable_count, yearly_revenue, activity_index, days_active, price_flat,  test_expired, pricing_type, billing_interval, payment_type))
					conn.commit()
					print ("here after commit")

			#curs.execute(etl_delta_load.delta_query[collection_name[:-5]])
			#conn.commit()

			print("finished parsing data for: "+collection_name)

		except Exception as e:
			param.counter-1
			#print ("exception")
			conn.rollback()
			curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
			.format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e), 'fail'))
			conn.commit()
			conn.close()
			curs.close()

		finally:
			conn.close()
			curs.close()