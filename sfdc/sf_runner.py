
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: main program to run the ETL process for sales force.
          This script uses beatbox for utilizing SOAP API provided 
          by sales force to extract the data. This script also does
          not work with python version > 2.7
"""

import psycopg2
import psycopg2.extras
import sys
import os
import time
from sf_exporter import Exporter
from sf_param import param
from sf_importer import Importer
import sf_importer
import threading
import queries



# perform no_op load from postgres
psycopg2.extras.register_default_json(loads=lambda x: x)
psycopg2.extras.register_default_jsonb(loads=lambda x: x)


if not os.path.exists(param.newpath):
    os.makedirs(param.newpath)

#20
param.counter = 1


print("Running ETL for  " +str(param.start_date) +" - " +str(param.end_date))


# runner19 = Exporter(queries.specs__c +param.rows,'specs__c', col = queries.specs__c.split(','))
# runner19.start()

# runner12 = Exporter(queries.account +param.rows,'account', col = queries.account.split(','))
# runner12.start()

# runner6 = Exporter(queries.lead +param.rows,'lead', col = queries.lead.split(','))
# runner6.start()

# runner = Exporter(queries.onb2__invoice__c +param.rows,'onb2__invoice__c', col = queries.onb2__invoice__c.split(','))
# runner.start()

# runner2 = Exporter(queries.onb2__item__c +param.rows,'onb2__item__c', col = queries.onb2__item__c.split(','))
# runner2.start()

# runner3 = Exporter(queries.onb2__subscription__c +param.rows,'onb2__subscription__c', col = queries.onb2__subscription__c.split(','))
# runner3.start()

# runner4 = Exporter(queries.onb2__dunning__c +param.rows,'onb2__dunning__c', col = queries.onb2__dunning__c.split(','))
# runner4.start()

# runner5 = Exporter(queries.onb2__dunningdetail__c +param.rows,'onb2__dunningdetail__c', col = queries.onb2__dunningdetail__c.split(','))
# runner5.start()


# runner8 = Exporter(queries.contract +param.rows,'contract', col = queries.contract.split(','))
# runner8.start()

# runner9 = Exporter(queries.recordtype +param.rows,'recordtype', col = queries.recordtype.split(','))
# runner9.start()

# runner7 = Exporter(queries.user +param.rows,'users', col = queries.user.split(','))
# runner7.start()

runner30 = Exporter(queries.case_churn +param.rows+" and RecordTypeId='012b0000000DheeAAC'", 'case_churn', col=queries.case_churn.split(','))
runner30.start()


# while param.counter != 0:
# 	sf_importer.import_data()

# 	if len(param.exported_table) == 10:
# 		runner10 = Exporter(queries.onb2__balance__c +param.rows,'onb2__balance__c', col = queries.onb2__balance__c.split(','))
# 		runner10.start()

# 		runner11 = Exporter(queries.contact +param.rows,'contact', col = queries.contact.split(','))
# 		runner11.start()

# 		runner13 = Exporter(queries.opportunity +param.rows,'opportunity', col = queries.opportunity.split(','))
# 		runner13.start()

# 		runner15 = Exporter(queries.onb2__dunningrun__c +param.rows,'onb2__dunningrun__c', col = queries.onb2__dunningrun__c.split(','))
# 		runner15.start()

# 		runner16 = Exporter(queries.onb2__invoicelineitem__c +param.rows,'onb2__invoicelineitem__c', col = queries.onb2__invoicelineitem__c.split(','))
# 		runner16.start()

# 		runner17 = Exporter(queries.onb2__invoicerun__c +param.rows,'onb2__invoicerun__c', col = queries.onb2__invoicerun__c.split(','))
# 		runner17.start()

# 		runner18 = Exporter(queries.asset +param.rows,'asset', col = queries.asset.split(','))
# 		runner18.start()

# 		runner14 = Exporter(queries.leadhistory +param.rows_leadhistory,'leadhistory', col = queries.leadhistory.split(','))
# 		runner14.start()

# 		runner20 = Exporter(queries.order +param.rows,'order', col = queries.order.split(','))
# 		runner20.start()

# 		runner30 = Exporter(queries.case_churn +param.rows, 'case_churn', col=queries.case_churn.split(','))
# 		runner30.start()

# 		param.exported_table.append('Stop Iteration !')
















