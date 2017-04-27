
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from param import param

delta_query = { 

# newsletters
'company': "drop table if exists company_id; create temp table company_id as select distinct id from absence.company where modified>='" +str(param.start_date) +"' and  modified<'" +str(param.end_date) +"';delete from stage.s_company_absence where id in (select id from company_id); insert into stage.s_company_absence select * from (select *,row_number() over (partition by id order by modified desc) as rnk from absence.company where modified>='" +str(param.start_date) +"' and  modified<'" +str(param.end_date) +"') as t where rnk=1;"
#,'custom_attribute_definitions': "drop table if exists custom_attribute_definitions_id; create temp table custom_attribute_definitions_id as select distinct id from absence.custom_attribute_definitions where modified>='" +str(param.start_date) +"' and  modified<'" +str(param.end_date) +"';delete from stage.s_custom_attribute_definitions_cs where id in (select id from custom_attribute_definitions_id); insert into stage.s_custom_attribute_definitions_cs select * from (select *,row_number() over (partition by id order by modified desc) as rnk from absence.custom_attribute_definitions where modified>='" +str(param.start_date) +"' and  modified<'" +str(param.end_date) +"') as t where rnk=1;"
}





