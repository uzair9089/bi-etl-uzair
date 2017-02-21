import os
import json
import sys
from sqlalchemy import create_engine
from threading import Thread, Lock
import psycopg2
from param import param
reload(sys)

class CustomCustomerAttributes:

    def parser(self, collection_name):

        try:

          conn_string = param.conn_bi
          conn = psycopg2.connect(conn_string)
          curs = conn.cursor()

          file = open(param.root+collection_name,'r')
          for line in file:
            x = json.loads(line,strict=False) 
            keys_in_record = x.keys()
             
            _id_oid = required = created_at = updated_at = valid_values = multivalue = uid = value_type = events_id = _id = slugs = booking = name = ''

            if '_id' in keys_in_record:
                if '$oid' in x["_id"]:
                    _id_oid = str(x["_id"]["$oid"])
            if 'required' in keys_in_record:
                required = str(x["required"])
            if 'created_at' in keys_in_record:
                if '$date' in x["created_at"]:
                    created_at = str(x["created_at"]["$date"])
            if 'updated_at' in keys_in_record:
                if '$date' in x["updated_at"]:
                    updated_at = str(x["updated_at"]["$date"])
            if 'valid_values' in keys_in_record:
                valid_values = str(x["valid_values"]).replace("u'","").replace("'","")
            if 'multivalue' in keys_in_record:
                multivalue = str(x["multivalue"])
            if 'uid' in keys_in_record:
                uid = str(x["uid"])
            if 'value_type' in keys_in_record:
                value_type = str(x["value_type"])
            if 'events_id' in keys_in_record:
                events_id = str(x["events_id"]).replace("u'","").replace("'","")
            if 'slugs' in keys_in_record:
                slugs = str(x["slugs"][0])
            if 'booking' in keys_in_record:
                booking = str(x["booking"])
            if 'name' in keys_in_record:
                name = str(x["name"])

            curs.execute("insert into cs.customer_custom_attributes(_id_oid, required, created_at, updated_at, valid_values, multivalue, uid, value_type, events_id,  slugs, booking, name) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')"
                .format(_id_oid, required, created_at, updated_at, valid_values, multivalue, uid, value_type, events_id, slugs, booking, name))
            conn.commit()

            conn.close()
            curs.close()

        except Exception as e:

            print(str(e))
            param.counter-1
            conn.rollback()
            curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
                .format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e), 'fail'))
            conn.commit()
            conn.close()
            curs.close()

        finally:

            conn.close()
            curs.close()



