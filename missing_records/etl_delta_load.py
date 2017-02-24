
""""
Author: Sanjiv Upadhyaya"
Date: 2016-10-03"
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database."
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL"
"""

from param import param

delta_query = { 
# core"
#'appointment_series': "create temp table appointment_series as select  a.* from missing_records.appointment_series a left join core.appointment_series b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at>='"+str(param.start_date)+"' and b.updated_at<'"+str(param.end_date)+"' b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.appointment_series select * from appointment_series; insert into stage.s_appointment_series select * from appointment_series;"
#'appointment_series': "create temp table appointment_series as select  a.* from missing_records.appointment_series a left join core.appointment_series b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.appointment_series select * from appointment_series; insert into stage.s_appointment_series select * from appointment_series;"
'closing_times': " create temp table closing_times as select  a.* from missing_records.closing_times a left join core.closing_times b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.closing_times select * from closing_times; insert into stage.s_appointment_series select * from appointment_series;"

,'customer_custom_attributes': " create temp table customer_custom_attributes as select   a.* from missing_records.customer_custom_attributes a left join core.customer_custom_attributes b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.customer_custom_attributes select * from customer_custom_attributes; insert into stage.s_appointment_series select * from appointment_series;"

,'shifts': " create temp table shifts as select   a.* from missing_records.shifts a left join core.shifts b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.shifts select * from shifts; insert into stage.s_appointment_series select * from appointment_series;"

,'shift_plan_templates': " create temp table shift_plan_templates as select  a.* from missing_records.shift_plan_templates a left join core.shift_plan_templates b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.shift_plan_templates select * from shift_plan_templates; insert into stage.s_appointment_series select * from appointment_series;"

,'appointment_series': " create temp table appointment_series as select  a.* from missing_records.appointment_series a left join core.appointment_series b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.appointment_series select * from appointment_series; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_key_accounts': " create temp table merchant_key_accounts as select  a.* from missing_records.merchant_key_accounts a left join core.merchant_key_accounts b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_key_accounts select * from merchant_key_accounts; insert into stage.s_appointment_series select * from appointment_series;"

,'service_categories': " create temp table service_categories as select  a.* from missing_records.service_categories a left join core.service_categories b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.service_categories select * from service_categories; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_customer_tags': " create temp table merchant_customer_tags as select  a.* from missing_records.merchant_customer_tags a left join core.merchant_customer_tags b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_customer_tags select * from merchant_customer_tags; insert into stage.s_appointment_series select * from appointment_series;"

,'newsletter_blacklists': " create temp table newsletter_blacklists as select  a.* from missing_records.newsletter_blacklists a left join core.newsletter_blacklists b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.newsletter_blacklists select * from newsletter_blacklists; insert into stage.s_appointment_series select * from appointment_series;"

,'notification_channels': " create temp table notification_channels as select  a.* from missing_records.notification_channels a left join core.notification_channels b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.notification_channels select * from notification_channels; insert into stage.s_appointment_series select * from appointment_series;"

,'pdf_forms': " create temp table pdf_forms as select  a.* from missing_records.pdf_forms a left join core.pdf_forms b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.pdf_forms select * from pdf_forms; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_customer_custom_attributes': " create temp table merchant_customer_custom_attributes as select  a.* from missing_records.merchant_customer_custom_attributes a left join core.merchant_customer_custom_attributes b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_customer_custom_attributes select * from merchant_customer_custom_attributes; insert into stage.s_appointment_series select * from appointment_series;"

,'uberall_accounts': " create temp table uberall_accounts as select  a.* from missing_records.uberall_accounts a left join core.uberall_accounts b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.uberall_accounts select * from uberall_accounts; insert into stage.s_appointment_series select * from appointment_series;"

,'employees': " create temp table employees as select  a.* from missing_records.employees a left join core.employees b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.employees select * from employees; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_permissions': " create temp table merchant_permissions as select  a.* from missing_records.merchant_permissions a left join core.merchant_permissions b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_permissions select * from merchant_permissions; insert into stage.s_appointment_series select * from appointment_series;"

,'newsletters': " create temp table newsletters as select  a.* from missing_records.newsletters a left join core.newsletters b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.newsletters select * from newsletters; insert into stage.s_appointment_series select * from appointment_series;"

,'appointment_services': " create temp table appointment_services as select  a.* from missing_records.appointment_services a left join core.appointment_services b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.appointment_services select * from appointment_services; insert into stage.s_appointment_series select * from appointment_series;"

,'event_participants': " create temp table event_participants as select  a.* from missing_records.event_participants a left join core.event_participants b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.event_participants select * from event_participants; insert into stage.s_appointment_series select * from appointment_series;"

,'customers': " create temp table customers as select  a.* from missing_records.customers a left join core.customers b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.customers select * from customers; insert into stage.s_appointment_series select * from appointment_series;"

,'feedbacks': " create temp table feedbacks as select  a.* from missing_records.feedbacks a left join core.feedbacks b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.feedbacks select * from feedbacks; insert into stage.s_appointment_series select * from appointment_series;"

,'events': " create temp table events as select  a.* from missing_records.events a left join core.events b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.events select * from events; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_accounts': " create temp table merchant_accounts as select  a.* from missing_records.merchant_accounts a left join core.merchant_accounts b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_accounts select * from merchant_accounts; insert into stage.s_appointment_series select * from appointment_series;"

,'resources': " create temp table resources as select  a.* from missing_records.resources a left join core.resources b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.resources select * from resources; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_profiles': " create temp table merchant_profiles as select  a.* from missing_records.merchant_profiles a left join core.merchant_profiles b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_profiles select * from merchant_profiles; insert into stage.s_appointment_series select * from appointment_series;"

,'services': " create temp table services as select  a.* from missing_records.services a left join core.services b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.services select * from services; insert into stage.s_appointment_series select * from appointment_series;"

,'merchant_customers': " create temp table merchant_customers as select  a.* from missing_records.merchant_customers a left join core.merchant_customers b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.merchant_customers select * from merchant_customers; insert into stage.s_appointment_series select * from appointment_series;"

,'appointment_resources': " create temp table appointment_resources as select  a.* from missing_records.appointment_resources a left join core.appointment_resources b ON a.updated_at = b.updated_at and a.id = b.id WHERE b.updated_at is NULL and b.id is null AND a.updated_at is not NULL and a.id is not NULL; insert into core.appointment_resources select * from appointment_resources; insert into stage.s_appointment_series select * from appointment_series;"


}
