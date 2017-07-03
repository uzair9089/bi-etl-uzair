
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03, what the fuck codes? need to refactor all the comments and unnecessary stuff 
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from param import param

# dictionary for storing truncate queries for tables without the date attributes. This hash is called immediately after csv dumps and before importing into dwh
truncate_queries = {
					# star
					'fact_appointments': "truncate table star.fact_appointments;"
					,'fact_feedbacks': "truncate table star.fact_feedbacks;"
					,'appointments': "truncate table star.appointments;"
					,'merchant_permissions': "truncate table star.merchant_permissions;"
					,'mobile_appointments': "truncate table star.mobile_appointments;"

					# growth cube
					,'list_date_02': "truncate table pentaho.list_date_02;"
					,'list_sfdc_accounts': "truncate table pentaho.list_sfdc_accounts;"
					,'list_city': "truncate table pentaho.list_city;"
					,'list_industry': "truncate table pentaho.list_industry;"
					,'list_subscription_channel': "truncate table pentaho.list_subscription_channel;"
					,'list_subscription_status': "truncate table pentaho.list_subscription_status;"
					,'list_subscription_start_date': "truncate table pentaho.list_subscription_start_date;"
					,'list_subscription_end_date': "truncate table pentaho.list_subscription_end_date;"
					,'fact_growth_general': "truncate table pentaho.fact_growth_general;"
					,'list_owner': "truncate table pentaho.list_owner;"

					# key account 
					,'list_created_by_merchant': "truncate table pentaho.list_created_by_merchant;"
					,'list_state': "truncate table pentaho.list_state;"
					,'given_feedbacks': "truncate table pentaho.given_feedbacks;"
					,'list_date': "truncate table pentaho.list_date;"
					,'list_hour': "truncate table pentaho.list_hour;"
					,'list_key_accounts_account': "truncate table pentaho.list_key_accounts_account;"
					,'list_widget_in_date': "truncate table pentaho.list_widget_in_date;"
					,'fact_key_accounts_appointments': "truncate table pentaho.fact_key_accounts_appointments;"

					# from dmart and dmart finance schemas
					,'ranking_coach_week_report_call': "truncate table star.ranking_coach_week_report_call;"
					, 'ranking_coach_week_report_web': "truncate table star.ranking_coach_week_report_web;"
					, 'salesforce_accounts': "truncate table star.salesforce_accounts;"
					, 'absence_mrr_development': "truncate table star.absence_mrr_development;"
					, 'adjustments_recurly': "truncate table star.adjustments_recurly;"
					, 'invoices_recurly': "truncate table star.invoices_recurly;"

				}

# this query is not executed because the redshift is very slow to handle this kind of query as a result it is not used at the time being
delta_query = {
				'customer_custom_attributes': "drop table if exists customer_custom_attributes_id; create temp table customer_custom_attributes_id as select distinct id from star.customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_customer_custom_attributes where id in (select id from customer_custom_attributes_id); insert into stage.s_customer_custom_attributes select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'employees': "drop table if exists employees_id; create temp table employees_id as select distinct id from star.employees where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_employees where id in (select id from employees_id); insert into stage.s_employees select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.employees where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'feedbacks': "drop table if exists feedbacks_id; create temp table feedbacks_id as select distinct id from star.feedbacks where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_feedbacks where id in (select id from feedbacks_id); insert into stage.s_feedbacks select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.feedbacks where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'event_participants': "drop table if exists event_participants_id; create temp table event_participants_id as select distinct id from star.event_participants where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_event_participants where id in (select id from event_participants_id); insert into stage.s_event_participants select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.event_participants where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'events': "drop table if exists events_id; create temp table events_id as select distinct id from star.events where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_events where id in (select id from events_id); insert into stage.s_events select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.events where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'merchant_customer_custom_attributes': "drop table if exists merchant_customer_custom_attributes_id; create temp table merchant_customer_custom_attributes_id as select distinct id from star.merchant_customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_customer_custom_attributes where id in (select id from merchant_customer_custom_attributes_id); insert into stage.s_merchant_customer_custom_attributes select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.merchant_customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'merchant_customer_tags': "drop table if exists merchant_customer_tags_id; create temp table merchant_customer_tags_id as select distinct id from star.merchant_customer_tags where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_customer_tags where id in (select id from merchant_customer_tags_id); insert into stage.s_merchant_customer_tags select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.merchant_customer_tags where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'merchant_customers': "drop table if exists merchant_customers_id; create temp table merchant_customers_id as select distinct id from star.merchant_customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_customers where id in (select id from merchant_customers_id); insert into stage.s_merchant_customers select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.merchant_customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'merchant_key_account_feature_toggles': "drop table if exists merchant_key_account_feature_toggles_id; create temp table merchant_key_account_feature_toggles_id as select distinct id from star.merchant_key_account_feature_toggles where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_key_account_feature_toggles where id in (select id from merchant_key_account_feature_toggles_id); insert into stage.s_merchant_key_account_feature_toggles select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.merchant_key_account_feature_toggles where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'merchant_key_accounts': "drop table if exists merchant_key_accounts_id; create temp table merchant_key_accounts_id as select distinct id from star.merchant_key_accounts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_key_accounts where id in (select id from merchant_key_accounts_id); insert into stage.s_merchant_key_accounts select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.merchant_key_accounts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'merchant_roles': "drop table if exists merchant_roles_id; create temp table merchant_roles_id as select distinct id from star.merchant_roles where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_roles where id in (select id from merchant_roles_id); insert into stage.s_merchant_roles select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.merchant_roles where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'resources': "drop table if exists resources_id; create temp table resources_id as select distinct id from star.resources where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_resources where id in (select id from resources_id); insert into stage.s_resources select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.resources where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'services': "drop table if exists services_id; create temp table services_id as select distinct id from star.services where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_services where id in (select id from services_id); insert into stage.s_services select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.services where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
				,'shifts': "drop table if exists shifts_id; create temp table shifts_id as select distinct id from star.shifts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_shifts where id in (select id from shifts_id); insert into stage.s_shifts select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from star.shifts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"


				,'fact_appointments': "select 1;"
				,'mobile_appointments': "select 1;"
				,'fact_feedbacks': "select 1;"
				,'appointments': "select 1;"
				,'merchant_permissions': "select 1;"


				,'list_date_02': "select 1;"
				,'list_sfdc_accounts': "select 1;"
				,'list_city': "select 1;"
				,'list_industry': "select 1;"
				,'list_subscription_channel': "select 1;"
				,'list_subscription_status': "select 1;"
				,'list_subscription_start_date': "select 1;"
				,'list_subscription_end_date': "select 1;"
				,'fact_growth_general': "select 1;"
				,'list_owner': "select 1;"

				# key account 
				,'list_created_by_merchant': "select 1;"
				,'list_state': "select 1;"
				,'given_feedbacks': "select 1;"
				,'list_date': "select 1;"
				,'list_hour': "select 1;"
				,'list_key_accounts_account': "select 1;"
				,'list_widget_in_date': "select 1;"
				,'fact_key_accounts_appointments': "select 1;"



				,'ranking_coach_week_report_call': "select 1;"
				, 'ranking_coach_week_report_web': "select 1;"
				, 'salesforce_accounts': "select 1;"
				,'absence_mrr_development': "select 1;"
				, 'adjustments_recurly': "select 1;"
				, 'invoices_recurly': "select 1;"

				}
