
"""
Author: Sanjiv Upadhyaya
Date: 2017-05-03
Function 1: remove the records existing in the stage database so that it is in sync with the application prod database.
Function 2: load data into staging in incremental way i.e, load data every 1 hours from the ETL
"""

from param import param

delta_query = { 

# company
'company': "drop table if exists company_id; create temp table company_id as select distinct id from absence.company where modified>='" +str(param.start_date) +"' and  modified<'" +str(param.end_date) +"';delete from stage.s_company_absence where id in (select id from company_id); insert into stage.s_company_absence select * from (select *,row_number() over (partition by id order by modified desc) as rnk from absence.company where modified>='" +str(param.start_date) +"' and  modified<'" +str(param.end_date) +"') as t where rnk=1;"
,'invoices': "truncate table stage.s_invoices; insert into stage.s_invoices select * from absence.invoices;"
}





