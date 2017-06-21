
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
					,'appointment_series': "truncate table star.appointment_series;"
					,'merchant_permissions': "truncate table star.merchant_permissions;"
					,'mobile_appointments': "truncate table star.mobile_appointments;"

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



