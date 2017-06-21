
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from param import param

# dictionary for storing truncate queries for tables without the date attributes. This hash is called immediately after csv dumps and before importing into dwh
truncate_queries = {
					# star
					,'fact_appointments': "truncate table star.fact_appointments;"
					,'fact_feedbacks': "truncate table star.fact_feedbacks;"
					,'appointments': "truncate table star.appointments;"
					,'appointment_series': "truncate table star.appointment_series;"

					# growth cube
					,'list_date_02': "truncate table pentaho.list_date_02"
					,'list_sfdc_accounts': "truncate table pentaho.list_sfdc_accounts"
					,'list_city': "truncate table pentaho.list_city"
					,'list_industry': "truncate table pentaho.list_industry"
					,'list_subscription_channel': "truncate table pentaho.list_subscription_channel"
					,'list_subscription_status': "truncate table pentaho.list_subscription_status"
					,'list_subscription_start_date': "truncate table pentaho.list_subscription_start_date"
					,'list_subscription_end_date': "truncate table pentaho.list_subscription_end_date"
					,'fact_growth_general': "truncate table pentaho.fact_growth_general"
					,'list_owner': "truncate table pentaho.list_owner"

					# key account 
					,'list_created_by_merchant': "truncate table pentaho.list_created_by_merchant"
					,'list_state': "truncate table pentaho.list_state"
					,'given_feedbacks': "truncate table pentaho.given_feedbacks"
					,'list_date': "truncate table pentaho.list_date"
					,'list_hour': "truncate table pentaho.list_hour"
					,'list_key_accounts_account': "truncate table pentaho.list_key_accounts_account"
					,'list_widget_in_date': "truncate table pentaho.list_widget_in_date"
					,'fact_key_accounts_appointments': "truncate table pentaho.fact_key_accounts_appointments"

				}




delta_query = { 
			# star
			,'fact_appointments': "truncate table stage.s_fact_appointments; insert into stage.s_fact_appointments select * from star.fact_appointments;"
			,'fact_feedbacks': "truncate table stage.s_fact_feedbacks; insert into stage.s_fact_feedbacks select * from star.fact_feedbacks;"
			,'appointments': "truncate table stage.s_appointments; insert into stage.s_appointments select * from star.appointments;"
			,'appointment_series': "truncate table stage.s_appointment_series; insert into stage.s_appointment_series select * from star.appointment_series;"

			# growth cube
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

		}


delete_queries = {

				# star
				,'fact_appointments': "truncate table stage.s_fact_appointments; insert into stage.s_fact_appointments select * from star.fact_appointments;"
				,'fact_feedbacks': "truncate table stage.s_fact_feedbacks; insert into stage.s_fact_feedbacks select * from star.fact_feedbacks;"
				,'appointments': "truncate table stage.s_appointments; insert into stage.s_appointments select * from star.appointments;"
				,'appointment_series': "truncate table stage.s_appointment_series; insert into stage.s_appointment_series select * from star.appointment_series;"

				# growth cube
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

			}


delta_query_reset = { 
				# star
				,'fact_appointments': "truncate table stage.s_fact_appointments; insert into stage.s_fact_appointments select * from star.fact_appointments;"
				,'fact_feedbacks': "truncate table stage.s_fact_feedbacks; insert into stage.s_fact_feedbacks select * from star.fact_feedbacks;"
				,'appointments': "truncate table stage.s_appointments; insert into stage.s_appointments select * from star.appointments;"
				,'appointment_series': "truncate table stage.s_appointment_series; insert into stage.s_appointment_series select * from star.appointment_series;"
				
				# growth cube
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

}

