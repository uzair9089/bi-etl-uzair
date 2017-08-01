from datetime import  date, timedelta
from threading import Thread, Lock
from importer import Importer
from param import param
from subscription_parser import SubscriptionParser as sp
import datetime
import dateutil
import psycopg2
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import pprint
import json
import time
import os


class Exporter(Thread):
	__lock = Lock()


	def __init__(self, collection_name):
		Thread.__init__(self)
		self.collection_name = collection_name


	def run(self):


		try:
			conn_string = param.conn_bi
			conn = psycopg2.connect(conn_string)
			curs = conn.cursor()
			recurly_token = os.environ['recurly_api_key']

			# run only in case of history load
			if self.collection_name in param.history_objects: 
				response = requests.request("GET", param.url[self.collection_name] + param.filters[self.collection_name], headers=param.headers, auth=HTTPBasicAuth(recurly_token, ''))
			else:
				response = requests.request("GET", param.url[self.collection_name] + param.filters_new[self.collection_name], headers=param.headers, auth=HTTPBasicAuth(recurly_token, ''))

			xml_string = ET.fromstring(response.content)
			# set the exported_file to 1 so imported can start after csv is dumped

			if 'Link' in response.headers:
				while 'rel="next"' in response.headers['Link']:
					next_link = response.headers['Link']
					#print(next_link)
					if 'rel="start"' in next_link:
						start_pos = next_link.find('rel="start"') + 14
					else: 
						start_pos = 1
					end_pos = next_link.find('rel="next"') - 3
					xml_link = next_link[start_pos:end_pos]
					#print(xml_link)
					response = requests.request('GET', xml_link, headers=param.headers, auth=HTTPBasicAuth(recurly_token, '')) # need to put that in environment variables
					next_xml_string = ET.fromstring(response.content)
					next_xml_string_child = next_xml_string.getchildren()
					xml_string.extend(next_xml_string_child)

			do = sp()
			do.parser(xml_string)

		# catch the exception and put it into the etl_status if any
		except Exception as e:
			curs.execute("""INSERT INTO etl_status (start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",[param.start_date, param.end_date, param.schema, self.collection_name, param.root+self.collection_name+str(".json"), 'import', str(e),'fail'])
			conn.commit()
			conn.close()
			curs.close()

		finally:
			conn.close()
			curs.close()






