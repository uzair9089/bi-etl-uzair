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

class InvoiceParser:

  def parser(self, collection_name):

    try:

      conn_string = param.conn_bi
      conn = psycopg2.connect(conn_string)
      curs = conn.cursor()

      if collection_name in param.truncate_queries:
        curs.execute(param.truncate_queries[collection_name])
        curs.execute
        conn.commit()

      file = open(param.newpath+collection_name,'r')

      for line in file:
        x = json.loads(line,strict=False) 
        keys_in_record = x.keys() 
        print keys_in_record

        if 'data' in keys_in_record:

          for data_lines in x["data"]:
            invoice_id =  company = invoice_batch = items = _id = 'N/A' 
            billing_interval = payment_type = pricing_type = price_gross = invoice_counter = price_net = invoice_status = vat = 0
            invoice_month = bill_date = '9999-01-01'
            
            if 'invoiceId' in data_lines.keys():
              invoice_id = str(data_lines["invoiceId"]).replace("'","")
            print invoice_id

            if 'company' in data_lines.keys():
              company = data_lines["company"]
              print company

            if 'invoiceBatch' in data_lines.keys():
              invoice_batch = data_lines["invoiceBatch"]
              print invoice_batch

            if 'invoiceMonth' in data_lines.keys(): 
              invoice_month = str(data_lines["invoiceMonth"]).replace("'","")
              print invoice_month

            if 'billDate' in data_lines.keys():
              bill_date = str(data_lines["billDate"]).replace("'","")
              #email.replace("'","")
              print bill_date

            if 'items' in data_lines.keys():
              items = str(data_lines["items"]).replace("'","")
              print items

            if '_id' in data_lines.keys():
              _id = str(data_lines["_id"]).replace("'","")
              print _id

            if 'billingInterval' in data_lines.keys():
              billing_interval = data_lines["billingInterval"]
              print billing_interval

            if 'pricingType' in data_lines.keys():
              pricing_type = str(data_lines["pricingType"]).replace("'","")
              print pricing_type

            if 'priceGross' in data_lines.keys():
              price_gross = str(data_lines["priceGross"]).replace("'","")
              print price_gross

            if 'invoiceCounter' in data_lines.keys():
              invoice_counter = str(data_lines["invoiceCounter"]).replace("'","")
              print invoice_counter

            if 'priceNet' in data_lines.keys():
              price_net = str(data_lines["priceNet"]).replace("'","")
              print price_net

            if 'invoiceStatus' in data_lines.keys():
              invoice_status = str(data_lines["invoiceStatus"]).replace("'","")
              print invoice_status

            curs.execute("insert into absence.invoices(invoice_id, company, invoice_batch, invoice_month, bill_date, items, _id, billing_interval, payment_type, pricing_type, price_gross, invoice_counter, price_net, invoice_status, vat) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}',{7},{8},{9},{10},{11},{12},{13},{14})"
            .format(invoice_id, company, invoice_batch, invoice_month, bill_date, items, _id, billing_interval, payment_type, pricing_type, price_gross, invoice_counter, price_net, invoice_status, vat))
            conn.commit()

            #print ("insert into absence.invoices(invoice_id, company, invoice_batch, invoice_month, bill_date, items, _id, billing_interval, payment_type, pricing_type, price_gross, invoice_counter, price_net, invoice_status, vat) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}',{7},{8},{9},{10},{11},{12},{13},{14})"
            #.format(invoice_id, company, invoice_batch, invoice_month, bill_date, items, _id, billing_interval, payment_type, pricing_type, price_gross, invoice_counter, price_net, invoice_status, vat))
            #print ("here after commit")


      print("finished parsing data for: " + collection_name)

      print ("delta load starts ")
      curs.execute(delta_query[collection_name[:-5]])
      conn.commit()

    except Exception as e:
      param.counter-1
      print ("exception")
      conn.rollback()
      curs.execute("insert into etl_status(start_date, end_date, schema_name, table_name, file_path, error_phase, error_message, status) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
      .format(param.start_date, param.end_date, param.schema, collection_name, param.root+collection_name, 'parsing', str(e).replace("'",""), 'fail'))
      conn.commit()
      conn.close()
      curs.close()

    finally:
      conn.close()
      curs.close()