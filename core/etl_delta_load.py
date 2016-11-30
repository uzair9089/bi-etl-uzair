
"""
Author: Sanjiv Upadhyaya
Date: 2016-010-03
Function 1: remove the records existing in the stage database so that it is in sync with the applicatin prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from param import param

delta_query = { 

# newsletters
,'newsletters_nwsl': "drop table if exists newsletters_nwsl_id; create temp table newsletters_nwsl_id as select distinct id from nwsl.newsletters_nwsl where updated_at>='" +str(param.start_date) +"'' and  updated_at<'" +str(param.end_date) +"'';delete from stage.s_newsletters_nwsl where id in (select id from newsletters_nwsl_id); insert into stage.s_newsletters_nwsl select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from nwsl.newsletters_nwsl where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'newsletter_customers': "truncate table stage.s_newsletter_customers; insert into stage.s_newsletter_customers select * from nwsl.newsletter_customers;"

# messages
,'conversations': "drop table if exists conversations_id; create temp table conversations_id as select distinct id from msg.conversations where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_conversations where id in (select id from conversations_id); insert into stage.s_conversations select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from msg.conversations where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'group_senders': "drop table if exists group_senders_id; create temp table group_senders_id as select distinct id from msg.group_senders where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_group_senders where id in (select id from group_senders_id); insert into stage.s_group_senders select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from msg.group_senders where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'messages': "drop table if exists messages_id; create temp table messages_id as select distinct id from msg.messages where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_messages where id in (select id from messages_id); insert into stage.s_messages select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from msg.messages where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'participants': "drop table if exists participants_id; create temp table participants_id as select distinct id from msg.participants where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_participants where id in (select id from participants_id); insert into stage.s_participants select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from msg.participants where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_senders': "drop table if exists merchant_senders_id; create temp table merchant_senders_id as select distinct id from msg.merchant_senders where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_senders where id in (select id from merchant_senders_id); insert into stage.s_merchant_senders select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from msg.merchant_senders where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'conversation_senders': "truncate table stage.s_conversation_senders; insert into stage.s_conversation_senders select * from msg.conversation_senders;"

# core
,'newsletters': "drop table if exists newsletters_id; create temp table newsletters_id as select distinct id from core.newsletters where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_newsletters where id in (select id from newsletters_id); insert into stage.s_newsletters select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.newsletters where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'appointment_services': "drop table if exists appointment_services_id; create temp table appointment_services_id as select distinct id from core.appointment_services where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_appointment_services where id in (select id from appointment_services_id); insert into stage.s_appointment_services select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.appointment_services where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'customers': "drop table if exists customers_id; create temp table customers_id as select distinct id from core.customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_customers where id in (select id from customers_id); insert into stage.s_customers select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'event_participants': "drop table if exists event_participants_id; create temp table event_participants_id as select distinct id from core.event_participants where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_event_participants where id in (select id from event_participants_id); insert into stage.s_event_participants select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.event_participants where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'feedbacks': "drop table if exists feedbacks_id; create temp table feedbacks_id as select distinct id from core.feedbacks where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_feedbacks where id in (select id from feedbacks_id); insert into stage.s_feedbacks select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.feedbacks where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'events': "drop table if exists events_id; create temp table events_id as select distinct id from core.events where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_events where id in (select id from events_id); insert into stage.s_events select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.events where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_accounts': "drop table if exists merchant_accounts_id; create temp table merchant_accounts_id as select distinct id from core.merchant_accounts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_accounts where id in (select id from merchant_accounts_id); insert into stage.s_merchant_accounts select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.merchant_accounts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_profiles': "drop table if exists merchant_profiles_id; create temp table merchant_profiles_id as select distinct id from core.merchant_profiles where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_profiles where id in (select id from merchant_profiles_id); insert into stage.s_merchant_profiles select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.merchant_profiles where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'resources': "drop table if exists resources_id; create temp table resources_id as select distinct id from core.resources where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_resources where id in (select id from resources_id); insert into stage.s_resources select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.resources where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'services': "drop table if exists services_id; create temp table services_id as select distinct id from core.services where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_services where id in (select id from services_id); insert into stage.s_services select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.services where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_customers': "drop table if exists merchant_customers_id; create temp table merchant_customers_id as select distinct id from core.merchant_customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_customers where id in (select id from merchant_customers_id); insert into stage.s_merchant_customers select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.merchant_customers where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'appointment_resources': "drop table if exists appointment_resources_id; create temp table appointment_resources_id as select distinct id from core.appointment_resources where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_appointment_resources where id in (select id from appointment_resources_id); insert into stage.s_appointment_resources select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.appointment_resources where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'closing_times': "drop table if exists closing_times_id; create temp table closing_times_id as select distinct id from core.closing_times where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_closing_times where id in (select id from closing_times_id); insert into stage.s_closing_times select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.closing_times where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'customer_custom_attributes': "drop table if exists customer_custom_attributes_id; create temp table customer_custom_attributes_id as select distinct id from core.customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_customer_custom_attributes where id in (select id from customer_custom_attributes_id); insert into stage.s_customer_custom_attributes select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_customer_tags': "drop table if exists merchant_customer_tags_id; create temp table merchant_customer_tags_id as select distinct id from core.merchant_customer_tags where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_customer_tags where id in (select id from merchant_customer_tags_id); insert into stage.s_merchant_customer_tags select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.merchant_customer_tags where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'newsletter_blacklists': "drop table if exists newsletter_blacklists_id; create temp table newsletter_blacklists_id as select distinct id from core.newsletter_blacklists where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_newsletter_blacklists where id in (select id from newsletter_blacklists_id); insert into stage.s_newsletter_blacklists select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.newsletter_blacklists where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'notification_channels': "drop table if exists notification_channels_id; create temp table notification_channels_id as select distinct id from core.notification_channels where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_notification_channels where id in (select id from notification_channels_id); insert into stage.s_notification_channels select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.notification_channels where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'pdf_forms': "drop table if exists pdf_forms_id; create temp table pdf_forms_id as select distinct id from core.pdf_forms where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_pdf_forms where id in (select id from pdf_forms_id); insert into stage.s_pdf_forms select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.pdf_forms where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'service_categories': "drop table if exists service_categories_id; create temp table service_categories_id as select distinct id from core.service_categories where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_service_categories where id in (select id from service_categories_id); insert into stage.s_service_categories select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.service_categories where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_customer_custom_attributes': "drop table if exists merchant_customer_custom_attributes_id; create temp table merchant_customer_custom_attributes_id as select distinct id from core.merchant_customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_merchant_customer_custom_attributes where id in (select id from merchant_customer_custom_attributes_id); insert into stage.s_merchant_customer_custom_attributes select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.merchant_customer_custom_attributes where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'uberall_accounts': "drop table if exists uberall_accounts_id; create temp table uberall_accounts_id as select distinct id from core.uberall_accounts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_uberall_accounts where id in (select id from uberall_accounts_id); insert into stage.s_uberall_accounts select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.uberall_accounts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'shifts': "drop table if exists shifts_id; create temp table shifts_id as select distinct id from core.shifts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_shifts where id in (select id from shifts_id); insert into stage.s_shifts select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.shifts where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'shift_plan_templates': "drop table if exists shift_plan_templates_id; create temp table shift_plan_templates_id as select distinct id from core.shift_plan_templates where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_shift_plan_templates where id in (select id from shift_plan_templates_id); insert into stage.s_shift_plan_templates select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.shift_plan_templates where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'appointment_series': "drop table if exists appointment_series_id; create temp table appointment_series_id as select distinct id from core.appointment_series where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_appointment_series where id in (select id from appointment_series_id); insert into stage.s_appointment_series select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from core.appointment_series where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'merchant_permissions': "truncate table stage.s_merchant_permissions; insert into stage.s_merchant_permissions select * from core.merchant_permissions;"
,'employees': "truncate table stage.s_employees; insert into stage.s_employees select * from core.employees;"
,'merchant_key_accounts': "truncate table stage.s_merchant_key_accounts; insert into stage.s_merchant_key_accounts select * from core.merchant_key_accounts;"

# intercom
,'companies_intercom':"truncate table stage.s_companies_intercom; insert into stage.s_companies_intercom select * from intercom.companies_intercom;"
,'segments_intercom':"truncate table stage.s_segments_intercom; insert into stage.s_segments_intercom select * from intercom.segments_intercom;"
,'contacts_intercom':"truncate table stage.s_contacts_intercom; insert into stage.s_contacts_intercom select * from intercom.contacts_intercom;"
,'tags_intercom':"truncate table stage.s_tags_intercom; insert into stage.s_tags_intercom select * from intercom.tags_intercom;"
,'users_intercom':"truncate table stage.s_users_intercom; insert into stage.s_users_intercom select * from intercom.users_intercom;"
,'conversations_intercom':"truncate table stage.s_conversations_intercom; insert into stage.s_conversations_intercom select * from intercom.conversations_intercom;"
,'conversation_parts_intercom':"truncate table stage.s_conversation_parts_intercom; insert into stage.s_conversation_parts_intercom select * from intercom.conversation_parts_intercom;"
,'admins_intercom':"truncate table stage.s_admins_intercom; insert into stage.s_admins_intercom select * from intercom.admins_intercom;"

# payment
,'disputes': "truncate table stage.s_disputes; insert into stage.s_disputes select * from pymt.disputes;"
,'bank_accounts': "truncate table stage.s_bank_accounts; insert into stage.s_bank_accounts select * from pymt.bank_accounts;"
,'request_logs': "truncate table stage.s_request_logs; insert into stage.s_request_logs select * from pymt.request_logs;"
,'stripe_events': "truncate table stage.s_stripe_events; insert into stage.s_stripe_events select * from pymt.stripe_events;"
,'charges': "truncate table stage.s_charges; insert into stage.s_charges select * from pymt.charges;"
,'merchants_pymt':"truncate table stage.s_merchants_pymt; insert into stage.s_merchants_pymt select * from pymt.merchants_pymt;"

# communication
,'merchants': "truncate table stage.s_merchants; insert into stage.s_merchants select * from comm.merchants;"
,'sms': "drop table if exists sms_id; create temp table sms_id as select distinct id from comm.sms where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_sms where id in (select id from sms_id); insert into stage.s_sms select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from comm.sms where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'emails': "drop table if exists emails_id; create temp table emails_id as select distinct id from comm.emails where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_emails where id in (select id from emails_id); insert into stage.s_emails select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from comm.emails where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"
,'publications': "drop table if exists publications_id; create temp table publications_id as select distinct id from comm.publications where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"';delete from stage.s_publications where id in (select id from publications_id); insert into stage.s_publications select * from (select *,row_number() over (partition by id order by updated_at desc) as rnk from comm.publications where updated_at>='" +str(param.start_date) +"' and  updated_at<'" +str(param.end_date) +"') as t where rnk=1;"

}







