"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: main program to run the ETL process.
"""

from exporter import Exporter
from importer import Importer
from param import param
import psycopg2.extras
import threading
import psycopg2
import importer
import datetime
import copy
import time
import sys
import os

# argument passed to ##runner program is stored in host variable
host = sys.argv[1]

param.dbconn(host)

# perform no_op load from postgres so that the json objects are treated as json instead of text or string
psycopg2.extras.register_default_json(loads=lambda x: x)
psycopg2.extras.register_default_jsonb(loads=lambda x: x)


DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: int(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)




# populate the source, truncating behaviour and table renaming schemes from the param file
def fetch_table(source_name):
    tbl_source = copy.copy(param.table_hash[source_name][0]['tbl_source'])
    tbl_source_truncate = copy.copy(param.table_hash[source_name][1]['tbl_source_truncate'])
    tbl_source_rename = copy.copy(param.table_hash[source_name][2]['tbl_source_rename'])
    tbl_all = copy.copy(tbl_source) + copy.copy(tbl_source_truncate)
    param.tbl_source = copy.copy(tbl_source)
    param.tbl_source_truncate = copy.copy(tbl_source_truncate)
    param.tbl_source_rename = copy.copy(tbl_source_rename)

    # setting tables which needs to be truncatted where table contains no date attributes
    truncate_table = []

    for table in tbl_source_truncate:
        if table in tbl_source_rename.keys():
            truncate_table.append(tbl_source_rename[table])
        else:
            truncate_table.append(table)

    # for adjusting the table name if it is to be renamed in the BI DWH because of potential similar name clash
    for table in tbl_all:
        if table in tbl_source_rename.keys():
            for table in tbl_source_rename.keys():
                tbl_all.remove(table)
                tbl_all.append(tbl_source_rename[table])
        else:
            pass

    
    param.exported_file = dict((el, 0) for el in tbl_all)
    param.truncate_tbl = copy.copy(truncate_table)




if not os.path.exists(param.newpath):
    os.makedirs(param.newpath)




if sys.argv[1] in param.sources:
    if param.reset_time == param.reset_value:
        print("Resetting data from " +str(param.reset_start_date) +" - " +str(param.reset_end_date))
    else:
        print("Running ETL for " +str(param.start_date) +" - " +str(param.end_date))



# filter_row/ filter_row_segment is used to filter the data based on the ETL start_date and end_date
if param.reset_time == param.reset_value:
    filter_row = " where updated_at >='" + str(param.reset_start_date) + "' and updated_at<'" + str(param.reset_end_date) + "'"
else:
    filter_row = " where updated_at >='" + str(param.start_date) + "' and updated_at<'" + str(param.end_date) + "'"
# filter_row = " "
filter_row_segment = " where updated_at::date >= current_date::date -1 and updated_at::date < current_date::date "



# if host in param.list_of_available_sources
if (host in param.sources):
    fetch_table(host)
    param.counter = len(param.tbl_source) + len(param.tbl_source_truncate)

    for i in param.tbl_source:
        print('extraction of ' + i + ' started')
        # handle the table renaming while importing the table

        if i in param.tbl_source_rename:
            runner = Exporter("select * from " + i + filter_row, param.tbl_source_rename[i]) #need to tackle the renamed tables
            runner.start()
            print('select * from ' + i, param.tbl_source_rename[i])

        else:
            runner = Exporter("select * from " + i + filter_row, i) #need to tackle the renamed tables
            runner.start()
            print('select * from ' + i, i)

    for j in param.tbl_source_truncate:
        print('extraction of ' + j + ' started')

        if j in param.tbl_source_rename:
            runner2 = Exporter('select * from '+ j, param.tbl_source_rename[j])
            runner2.start()
            print('select * from ' + j, param.tbl_source_rename[j])

        else:
            runner2 = Exporter('select * from '+ j, j)
            runner2.start()
            print('select * from ' + j, j)


# run the ETL process until all the mentioned tables in the param file are exported.
while param.counter != 0:
	importer.import_data()















