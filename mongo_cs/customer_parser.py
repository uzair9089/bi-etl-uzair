from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
import etl_delta_load
import psycopg2
import os
import json
import sys


reload(sys)

class CustomerParser:

  def parser(self, collection_name):

    try:

      conn_string = param.conn_bi
      conn = psycopg2.connect(conn_string)
      curs = conn.cursor()

      file = open(param.root+collection_name,'r')

      for line in file:
          x = json.loads(line,strict=False) 
          keys_in_record = x.keys() 

          _id  = name = value = email = first_name = last_name =  gender = city = country  = phones = tags = oid = deleted_at = uid = id_oid = vip = updated_at  = created_at = ''

          if 'dates' in keys_in_record:
            if '_id' in x["dates"][0]:
                _id = str(x["dates"][0]["_id"])

            if 'name' in x["dates"][0]:
                name = str(x["dates"][0]["name"])
                  

            if '$date' in x["dates"][0]["value"]:
                if '$date' in x["dates"][0]["value"]:
                  value = str(x["dates"][0]["value"]["$date"]).replace("u'","").replace("'","")
          if 'emails' in keys_in_record:
            if 'value' in x["emails"][0]:
                email = str(x["emails"][0]["value"])
          if 'addresses' in keys_in_record:
            if 'city' in x["addresses"][0] and x["addresses"][0]["city"]is not None:
                city = str(x["addresses"][0]["city"])
          if 'addresses' in keys_in_record:
            if 'country' in x["addresses"][0]:
                country = str(x["addresses"][0]["country"])
          if 'phones' in keys_in_record:
            if 'value' in x["phones"][0]:
                phones = str(x["phones"][0]["value"])
          if 'tags' in keys_in_record and x["tags"]!= []:
            tags = str(x["tags"]).replace("u'","").replace("'","")
          else:
            tags ='None'
          if 'oid' in keys_in_record:
            oid = str(x["oid"])
          if 'deleted_at' in keys_in_record:
            deleted_a = str(x["deleted_at"])
          if 'uid' in keys_in_record:
            uid = str(x["uid"])
          if '_id' in keys_in_record:
            id_oid = str(x["_id"]["$oid"])
          if 'vip' in keys_in_record:
            vip = str(x["vip"])
          if 'updated_at' in keys_in_record:
            if '$date' in x["updated_at"]:
                updated_at = str(x["updated_at"]["$date"])
          if 'created_at' in keys_in_record:
            if '$date' in x["created_at"]:
                created_at = str(x["created_at"]["$date"])
          if 'identity' in keys_in_record:
            if 'gender' in x["identity"]:
              gender = x["identity"]["gender"]
            if 'first' in x["identity"]:
              first_name = x["identity"]["first"]
            if 'last' in x["identity"]:
              last_name = x["identity"]["last"]

          curs.execute ("insert into cs.customers(id, name, value, email, city, country, phones, tags, oid, deleted_at, uid, id_oid, vip, updated_at, created_at, gender, first_name, last_name) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}')"
          .format(_id, name, value, email, city, country, phones, tags, oid, deleted_at, uid, id_oid, vip, updated_at, created_at, gender, first_name, last_name))
          curs.execute(etl_delta_load.delta_query[collection_name])
          conn.commit()

      conn.close()
      curs.close()


    except Exception as e:

      print(str(e))
      param.counter-1
      conn.rollback()
      #curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
      #    .format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e), 'fail'))
      conn.commit()
      conn.close()
      curs.close()

    finally:

      conn.close()
      curs.close()


