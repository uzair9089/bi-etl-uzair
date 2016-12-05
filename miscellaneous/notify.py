#!/usr/bin/python
from sqlalchemy import create_engine
import psycopg2
import smtplib
import os

conn_string = os.environ['conn_bi']
conn = psycopg2.connect(conn_string)
curs = conn.cursor()
curs.execute(("select count(*) from public.etl_status where status = {0}").format("'"+'fail'+"'"))
error_count = curs.fetchall()
sender = 'sanjivupadhyaya@shore.com'
receivers = ['su@shore.com']

try:
	if len(error_count)>1:
		message = """ ETL Process Status - Failure. Please check the etl status !
		"""
		try:
			smtpObj = smtplib.SMTP('localhost')
			smtpObj.sendmail(sender, receivers, message)         
			print "Successfully sent email"
			
		except SMTPException:
			print "Error: unable to send email"


except:
	message = """ ETL Process if just fine
	"""

