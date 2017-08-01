
"""
Author: Sanjiv Upadhyaya
Date: 2017-05-03
Function 1: remove the records existing in the stage database so that it is in sync with the application prod database.
Function 2: load data into staging in incremental way i.e, load data every 1 hours from the ETL
"""

from param import param

delta_query = {'subscriptions': "drop table if exists subscriptions_uuid; create temp table subscriptions_uuid as select distinct uuid from recurly.subscriptions where updated_at>='" +str(param.start_date) +"';delete from stage.s_subscriptions_recurly where uuid in (select uuid from subscriptions_uuid); insert into stage.s_subscriptions_recurly select * from (select *,row_number() over (partition by uuid order by updated_at desc) as rnk from recurly.subscriptions where updated_at>='" +str(param.start_date) +"') as t where rnk=1;"
				}


