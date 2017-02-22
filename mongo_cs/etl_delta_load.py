
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from param import param

delta_query = { 

# newsletters
'customers': "drop table if exists customers_id; create temp table customers_id as select distinct uuid from cs.customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_customers_cs where uuid in (select uuid from customers_id); insert into stage.s_customers_cs select * from (select *,row_number() over (partition by uuid order by updated_at desc) as rnk from cs.customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"

,'custom_attribute_definitions': "drop table if exists custom_attribute_definitions_id; create temp table custom_attribute_definitions_id as select distinct uuid from cs.custom_attribute_definitions where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_custom_attribute_definitions where id in (select uuid from custom_attribute_definitions_id); insert into stage.s_custom_attribute_definitions select * from (select *,row_number() over (partition by uuid order by updated_at desc) as rnk from cs.custom_attribute_definitions where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"

}







