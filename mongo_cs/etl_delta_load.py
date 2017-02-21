
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from param import param

delta_query = { 

# newsletters
'customers': "drop table if exists customers_id; create temp table customers_id as select distinct id from cs.customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_customers_cs where id in (select id from customers_id); insert into stage.s_customers_cs select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from cs.customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"

,'custom_customer_attributes': "drop table if exists custom_customer_attributes_id; create temp table custom_customer_attributes_id as select distinct id from cs.custom_customer_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_custom_customer_attributes where id in (select id from custom_customer_attributes_id); insert into stage.s_custom_customer_attributes select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from cs.custom_customer_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"

}







