#!/usr/bin/python
from sqlalchemy import create_engine
import psycopg2
import smtplib
import os

conn_string = os.environ['conn_bi']
conn = psycopg2.connect(conn_string)
curs = conn.cursor()
curs.execute(("select * from public.etl_status where status = {0}").format("'"+'fail'+"'"))
error_count = curs.fetchall()
sender = 'sanjivupadhyaya@shore.com'
receivers = ['su@shore.com']

if len(error_count)>0:
	message = """ ETL Process Status - Failure. Please check the etl status !
	"""
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, receivers, message)  
else:
	print("no error in the ETL process")

