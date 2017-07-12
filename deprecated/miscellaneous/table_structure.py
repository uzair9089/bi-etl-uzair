import sqlalchemy as sqa
import psycopg2.extras
import pandas as pd
import psycopg2
import os


# connection strings for various data sources
conn_string_core = os.environ['conn_core']
conn_string_msg = os.environ['conn_msg']
conn_string_comm = os.environ['conn_comm']
conn_string_pymt = os.environ['conn_pymt']
conn_string_nwsl = os.environ['conn_nwsl']
conn_string_bi = os.environ['conn_bi']

# query for checking the table structures from the pg_tables and information_schema.columns
query_prod_core = """select table_name,column_name from information_schema.columns where table_name
 in ('appointment_resources',
'appointment_series',
'appointment_services',
'customers',
'employees',
'event_participants',
'events',
'feedbacks',
'merchant_accounts',
'merchant_customers',
'merchant_key_accounts',
'merchant_profiles',
'newsletters',
'resources',
'services',
'shift_plan_templates',
'shifts',
'pdf_forms','merchant_customer_tags','customer_custom_attributes','notification_channels','newsletter_blacklists',
'service_categories','closing_times','merchant_customer_custom_attributes','uberall_accounts') order by table_name,column_name"""


query_prod_msg = """select table_name,column_name from information_schema.columns where table_name
 in ('conversations',
'conversation_senders',
'group_senders',
'merchant_senders',
'merchant_senders_bkp',
'messages',
'participants') order by table_name,column_name"""


query_prod_nwsl = """select table_name,column_name from information_schema.columns where table_name
 in ('newsletter_customers',
'newsletters'
) order by table_name,column_name"""


query_prod_pymt = """select table_name,column_name from information_schema.columns where table_name
 in ('bank_accounts',
'charges',
'disputes',
'request_logs',
'stripe_events') order by table_name,column_name"""

query_prod_comm = """select table_name,column_name from information_schema.columns where table_name
 in ('emails',
'merchants',
'publications',
'sms') order by table_name,column_name"""

query_bi_core = query_prod_core
query_bi_msg = query_prod_msg
query_bi_nwsl = query_prod_nwsl
query_bi_pymt = query_prod_pymt
query_bi_comm =  query_prod_comm

try:
    conn = psycopg2.connect(conn_string_core)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_prod_core)

    with open("prod_core.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))


try:
    conn = psycopg2.connect(conn_string_msg)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_prod_msg)

    with open("prod_msg.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))



try:
    conn = psycopg2.connect(conn_string_nwsl)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_prod_nwsl)

    with open("prod_nwsl.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))


try:
    conn = psycopg2.connect(conn_string_comm)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_prod_comm)

    with open("prod_comm.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))


try:
    conn = psycopg2.connect(conn_string_pymt)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_prod_pymt)

    with open("prod_pymt.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))


try:
    conn = psycopg2.connect(conn_string_bi)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_bi_core)

    with open("bi_core.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))



try:
    conn = psycopg2.connect(conn_string_bi)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_bi_msg)

    with open("bi_msg.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))



try:
    conn = psycopg2.connect(conn_string_bi)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_bi_nwsl)

    with open("bi_nwsl.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))


try:
    conn = psycopg2.connect(conn_string_bi)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_bi_comm)

    with open("bi_comm.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))


try:
    conn = psycopg2.connect(conn_string_bi)
    curs = conn.cursor()
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_bi_pymt)

    with open("bi_pymt.txt", 'w+') as f:
        curs.copy_expert(outputquery, f)

    curs.close()
    conn.close()


except Exception as e:
    print("Unable to access database, export error %s" % (str(e)))

with open('prod_core.txt') as f1, open('bi_core.txt') as f2, open('core.txt','w') as f3:
    for x, y in zip(f1, f2): 
        if x != y:
            f3.write(x)

with open('prod_msg.txt') as f1, open('bi_msg.txt') as f2, open('msg.txt','w') as f3:
    for x, y in zip(f1, f2): 
        if x != y:
            f3.write(x)


with open('prod_nwsl.txt') as f1, open('bi_nwsl.txt') as f2, open('nwsl.txt','w') as f3:
    for x, y in zip(f1, f2): 
        if x != y:
            f3.write(x)

with open('prod_comm.txt') as f1, open('bi_comm.txt') as f2, open('comm.txt','w') as f3:
    for x, y in zip(f1, f2): 
        if x != y:
            f3.write(x)

with open('prod_pymt.txt') as f1, open('bi_pymt.txt') as f2, open('pymt.txt','w') as f3:
    for x, y in zip(f1, f2): 
        if x != y:
            f3.write(x)


for files in ('core.txt','nwsl.txt','msg.txt','comm.txt','pymt.txt'):
    if (os.stat(files).st_size > 4):
        print("Change in the structure in: "+files[:-4])
        print("please check the file " +files+ " for details" )


