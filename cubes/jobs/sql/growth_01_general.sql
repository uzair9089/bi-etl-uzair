/**
This SQL Script is used to create Tables in the Data Warehouse Schema dmart. These tables are the basis for the Pentaho Cube called 'Growth_01_General_Cube'.
This cube has the following dimensions:
- City
- Country
- Industry
- Subscription Status
- Subscription Channel
- Subscription Start Date
- Subscription End Date
- Created Date Dimension with day as the minimum level
- # resources
- # services
It is a very general aggregation of the following Measures which can be displayed on the lowest aggregation level per Merchant per Day:
- gastrofix_payments
- amount
- online_payments
- amount
- emails
- sms
- messages
- conversations
- newsletters
- recipients
- feedbacks
- shifts
- bookings
- sma
*/

/**
Create Table and Index on City with all Cities based on Account.BillingCity
*/
DROP TABLE IF EXISTS dmart.list_city;
CREATE TABLE dmart.list_city AS (
	SELECT distinct ONB2__Subscription__c.ONB2__LegalCity__c As City, ONB2__Subscription__c.ONB2__LegalCountry__c As Country
	FROM prod.ONB2__Subscription__c
	WHERE ONB2__Subscription__c.ONB2__LegalCity__c NOTNULL
);
ALTER TABLE dmart.list_city ADD COLUMN id SERIAL PRIMARY KEY;

CREATE INDEX list_city_idx
  ON dmart.list_city
  USING btree
  (id);

/**
Create Table and Index on Industry Name with all Industries based on Account.Industry
*/
DROP TABLE IF EXISTS dmart.list_industry;
CREATE TABLE dmart.list_industry AS (
	SELECT distinct Industry 
	FROM prod.Account
	WHERE Industry NOTNULL
	AND refActiveSubscription__c NOTNULL
);
ALTER TABLE dmart.list_industry ADD COLUMN id SERIAL PRIMARY KEY;

CREATE INDEX list_industry_idx
  ON dmart.list_industry
  USING btree
  (id);

/**
Create Table and Index on Stati Name with Subscription Stati based on ONB2__Subscription__c.ONB2__Status__c
*/
DROP TABLE IF EXISTS dmart.list_subscription_status;
CREATE TABLE dmart.list_subscription_status AS (
	SELECT distinct ONB2__Status__c as subscription_status
	FROM prod.ONB2__Subscription__c
	WHERE ONB2__Status__c NOTNULL
);
ALTER TABLE dmart.list_subscription_status ADD COLUMN id SERIAL PRIMARY KEY;

CREATE INDEX list_subscription_status_idx
  ON dmart.list_subscription_status
  USING btree
  (id);

/**
Create Series of dates with Id, Date, full date, day of week, month, year, fiscal year month, holiday, weekend (month_id and order day of week are needed for ordering the text fields correctly)
*/
DROP TABLE IF EXISTS dmart.list_date_02;

CREATE TABLE IF NOT EXISTS dmart.list_date_02
(
  created_at_id serial,
  Date date,
  full_day_description text,
  day_of_week text,
  calendar_month text,
  calendar_year integer,
  fiscal_year_month text,
  holiday text,
  weekend text,
  month_id integer,
  order_day_of_week integer
);

INSERT INTO dmart.list_date_02
	(
	Date,
	full_day_description,
	day_of_week,
	calendar_month,
	calendar_year,
	fiscal_year_month,
	holiday,
	weekend,
	month_id,
	order_day_of_week
	)
SELECT
	day,
	rtrim(to_char(day, 'Month')) || to_char(day, ' DD, YYYY'),
	to_char(day, 'Day'),
	rtrim(to_char(day, 'Month')),
	date_part('year', day),
	'F' || to_char(day, 'YYYY-MM'),
	'', --omitting (trivial 'Holiday'/'Non-Holiday, but how to get this ??)
	CASE
	    WHEN date_part('isodow', day) IN (6, 7) THEN 'Weekend'
	    ELSE 'Weekday'
	END,
	CASE WHEN rtrim(to_char(day, 'Month')) = 'January' then 1 
		WHEN rtrim(to_char(day, 'Month')) = 'February' then 2
		WHEN rtrim(to_char(day, 'Month')) = 'March' then 3
		WHEN rtrim(to_char(day, 'Month')) = 'April' then 4
		WHEN rtrim(to_char(day, 'Month')) = 'May' then 5
		WHEN rtrim(to_char(day, 'Month')) = 'June' then 6
		WHEN rtrim(to_char(day, 'Month')) = 'July' then 7
		WHEN rtrim(to_char(day, 'Month')) = 'August' then 8
		WHEN rtrim(to_char(day, 'Month')) = 'September' then 9
		WHEN rtrim(to_char(day, 'Month')) = 'October' then 10
		WHEN rtrim(to_char(day, 'Month')) = 'November' then 11
		WHEN rtrim(to_char(day, 'Month')) = 'December' then 12 ELSE 0 END as month_id,

	CASE WHEN rtrim(to_char(day, 'Day')) = 'Monday' then 1 
		WHEN rtrim(to_char(day, 'Day')) = 'Tuesday' then 2
		WHEN rtrim(to_char(day, 'Day')) = 'Wednesday' then 3
		WHEN rtrim(to_char(day, 'Day')) = 'Thursday' then 4
		WHEN rtrim(to_char(day, 'Day')) = 'Friday' then 5
		WHEN rtrim(to_char(day, 'Day')) = 'Saturday' then 6
		WHEN rtrim(to_char(day, 'Day')) = 'Sunday' then 7
		END as order_day_of_week

FROM
    generate_series('2013-01-01'::date, current_date::date, '1 day') day;

CREATE INDEX list_date_02_date_idx
  ON dmart.list_date_02
  USING btree
  (date);

CREATE INDEX list_date_02_id_idx
  ON dmart.list_date_02
  USING btree
  (created_at_id);

/**
Duplicate list_date_02 in order to have same time dimensions for Subscription Start Date
*/
DROP TABLE if exists dmart.list_subscription_start_date;
CREATE TABLE dmart.list_subscription_start_date as select * from dmart.list_date_02;

CREATE INDEX list_subscription_start_date_idx
  ON dmart.list_subscription_start_date
  USING btree
  (date);

-- Duplicate list_date_02 in order to have same time dimensions for Subscription End Date
DROP TABLE if exists dmart.list_subscription_end_date;
CREATE TABLE dmart.list_subscription_end_date as select * from dmart.list_date_02;

CREATE INDEX list_subscription_end_date_idx
  ON dmart.list_subscription_end_date
  USING btree
  (date);

/**
Create Table and Index on Stati Name with Subscription Stati based on ONB2__Subscription__c.ONB2__Status__c
*/
DROP TABLE IF EXISTS dmart.list_subscription_channel;
CREATE TABLE dmart.list_subscription_channel AS (
	SELECT distinct fmlChannel__c as channel
	FROM prod.ONB2__Subscription__c
	WHERE fmlChannel__c NOTNULL
);
ALTER TABLE dmart.list_subscription_channel ADD COLUMN id SERIAL PRIMARY KEY;

CREATE INDEX list_subscription_channel_idx
  ON dmart.list_subscription_channel
  USING btree
  (id);

/**
Create SFDC Account List Table which serves as the basis for Salesforce data
*/
DROP TABLE IF EXISTS dmart.list_sfdc_accounts;
CREATE TABLE dmart.list_sfdc_accounts AS (
	SELECT Account.Id, Account.Name, Account.dShopId__c::integer as merchant_profile_id, Account.strMerchantUUID__c as merchant_uuid, 
	Account.dKeyAccountId__c::integer as merchant_key_account_id, 
	Account.dTotalActivityScore__c as activity_score, 
	ONB2__Subscription__c.lastmodifieddate,
	ONB2__Subscription__c.ONB2__startdate__c,
	list_city.id as city_id,
	list_industry.id as industry_id,
	list_subscription_status.id as subscription_status_id,
	list_subscription_channel.id as subscription_channel_id,
	list_subscription_start_date.created_at_id as subscription_start_id,
	list_subscription_end_date.created_at_id as subscription_end_id
	FROM prod.Account
	LEFT JOIN dmart.list_industry
	ON list_industry.Industry = Account.Industry
	LEFT JOIN dmart.list_subscription_status
	ON list_subscription_status.subscription_status = account.fmlSubscriptionStatus__c
	LEFT JOIN prod.onb2__subscription__c
	ON ONB2__Subscription__c.ONB2__Account__c = Account.Id
	LEFT JOIN dmart.list_city
	ON list_city.city = ONB2__Subscription__c.ONB2__LegalCity__c
	AND list_city.country = ONB2__Subscription__c.ONB2__LegalCountry__c
	LEFT JOIN dmart.list_subscription_channel
	ON list_subscription_channel.channel = onb2__subscription__c.fmlChannel__c
	LEFT JOIN dmart.list_subscription_start_date
	ON list_subscription_start_date.date = ONB2__Subscription__c.ONB2__StartDate__c
	LEFT JOIN dmart.list_subscription_end_date
	ON list_subscription_end_date.date = ONB2__Subscription__c.ONB2__EndDate__c
	WHERE dshopId__c NOTNULL
	AND refActiveSubscription__c NOTNULL
);


/**
The following part is used to get rid of duplicate merchant profile ids which lead to a cross join in creating the fact table
1. The duplicate accounts with the latest last modified date are chosen
2. Duplicate accounts with the latest subscription start date are chosen
These two steps eliminate the duplicate values.
*/
drop table if exists to_del;
create temp table to_del as select distinct merchant_profile_id as id, lastmodifieddate from dmart.list_sfdc_accounts;
drop table if exists dup_records;
create temp table dup_records as 
select * 
from (
   select id, 
          lastmodifieddate, 
          row_number() over (partition by id order by lastmodifieddate desc) as rnk
   from to_del
) as t
where rnk > 1
;
delete from dmart.list_sfdc_accounts where list_sfdc_accounts.merchant_profile_id in (select dup_records.id from dup_records) and list_sfdc_accounts.lastmodifieddate in(select dup_records.lastmodifieddate from dup_records);


drop table if exists to_del;
create temp table to_del as select distinct merchant_profile_id as id, ONB2__startdate__c from dmart.list_sfdc_accounts;
drop table if exists dup_records;
create temp table dup_records as 
select * 
from (
   select id, 
          ONB2__startdate__c, 
          row_number() over (partition by id order by ONB2__startdate__c desc) as rnk
   from to_del
) as t
where rnk > 1
;
delete from dmart.list_sfdc_accounts where list_sfdc_accounts.merchant_profile_id in (select dup_records.id from dup_records) and list_sfdc_accounts.ONB2__startdate__c in(select dup_records.ONB2__startdate__c from dup_records);

-- Index is created
CREATE INDEX list_sfdc_accounts_idx
  ON dmart.list_sfdc_accounts
  USING btree
  (merchant_profile_id);

/**
The two tables below are aggregated on Merchant Basis
*/
DROP TABLE IF EXISTS agg_resources;
CREATE TEMP TABLE agg_resources AS (
	SELECT merchant_profile_id, count(distinct id) as resource_count
	from prod.resources 
	where constraints_type IN ('employee', null)
	GROUP BY merchant_profile_id
);
DROP TABLE IF EXISTS agg_services;
CREATE TEMP TABLE agg_services AS (
	SELECT merchant_profile_id, count(distinct id) as service_count
	FROM prod.services
	GROUP BY merchant_profile_id
);

/**
The two tables below are aggregated per Merchant per day
Relevant KPIs in the temporary tables are:
- gastrofix_payments
- amount
- online_payments
- amount
- emails
- sms
- messages
- conversations
- newsletters
- recipients
- feedbacks
- shifts
- bookings
- sma
- service_count
- resource_count
*/
DROP TABLE IF EXISTS temp_sma;
CREATE TEMP TABLE temp_sma AS (
	SELECT list_date_02.created_at_id as date_id, 
	appointment_series.merchant_profile_id,
	count(distinct appointment_series.id) as sma
	FROM prod.appointment_series
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', appointment_series.created_at)::date
	WHERE appointment_series.created_by_merchant = true
	GROUP BY date_id, merchant_profile_id
);

DROP TABLE IF EXISTS temp_bookings;
CREATE TEMP TABLE temp_bookings AS (
	SELECT list_date_02.created_at_id as date_id, 
	appointment_series.merchant_profile_id,
	count(distinct appointment_series.id) as bookings
	FROM prod.appointment_series
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', appointment_series.created_at)::date
	WHERE appointment_series.created_by_merchant = false
	GROUP BY date_id, merchant_profile_id
);

DROP TABLE IF EXISTS temp_customers;
CREATE TEMP TABLE temp_customers AS (
	SELECT list_date_02.created_at_id as date_id,
	merchant_profile_id,
	count(distinct id) as customers
	FROM prod.merchant_customers
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', merchant_customers.created_at)::date
	GROUP BY date_id, merchant_profile_id
);

DROP TABLE IF EXISTS temp_feedbacks;
CREATE TEMP TABLE temp_feedbacks AS (
	SELECT list_date_02.created_at_id as date_id, 
	appointment_series.merchant_profile_id,
	count(distinct feedbacks.id) as feedbacks
	FROM prod.feedbacks
	INNER JOIN prod.appointment_series
	ON appointment_series.uuid = feedbacks.appointment_id
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', feedbacks.updated_at)::date
	WHERE feedbacks.state = 'given'
	GROUP BY date_id, merchant_profile_id
);

DROP TABLE IF EXISTS temp_shifts;
CREATE TEMP TABLE temp_shifts AS (
	SELECT list_date_02.created_at_id as date_id,
	resources.merchant_profile_id,
	count(distinct shifts.id) as shifts
	FROM prod.shifts
	INNER JOIN prod.resources
	ON resources.id = shifts.resource_id
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', shifts.starts_at)::date
	GROUP BY date_id, merchant_profile_id
);

DROP TABLE IF EXISTS temp_newsletters;
CREATE TEMP TABLE temp_newsletters AS (
	SELECT list_date_02.created_at_id as date_id,
	newsletters_nwsl.merchant_uuid,
	merchant_profiles.id as merchant_profile_id,
	count(distinct newsletters_nwsl.id) as newsletters,
	count(distinct newsletter_customers.customer_uuid) as recipients
	FROM prod.newsletters_nwsl
	LEFT JOIN prod.newsletter_customers
	ON newsletter_customers.newsletter_id = newsletters_nwsl.id
	INNER JOIN prod.merchant_profiles
	ON merchant_profiles.uuid = newsletters_nwsl.merchant_uuid
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', newsletters_nwsl.sent_at)::date
	Where newsletters_nwsl.sent_at NOTNULL
	AND newsletters_nwsl.state = 'sent'
	GROUP BY date_id, merchant_uuid, merchant_profile_id
);

DROP TABLE IF EXISTS temp_messages;
CREATE TEMP TABLE temp_messages AS (
	SELECT list_date_02.created_at_id as date_id,
	conversations.merchant_id as merchant_uuid,
	merchant_profiles.id as merchant_profile_id,
	count(distinct messages.id) as messages,
	count(distinct conversations.id) as conversations
	FROM prod.messages
	INNER JOIN prod.conversations
	ON conversations.id = messages.conversation_id
	INNER JOIN prod.merchant_profiles
	ON merchant_profiles.uuid = conversations.merchant_id
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', messages.created_at)::date
	GROUP BY date_id, conversations.merchant_id, merchant_profile_id
);

DROP TABLE IF EXISTS temp_sms;
CREATE TEMP TABLE temp_sms AS (
	SELECT list_date_02.created_at_id as date_id,
	sms.merchant_id as merchant_uuid,
	merchant_profiles.id as merchant_profile_id,
	sum(sms.segments) as sms
	FROM prod.sms
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', sms.sent_at)::date
	INNER JOIN prod.merchant_profiles
	ON merchant_profiles.uuid = sms.merchant_id
	WHERE sms.sent_at NOTNULL
	GROUP BY date_id, merchant_uuid, merchant_profile_id
);

DROP TABLE IF EXISTS temp_email;
CREATE TEMP TABLE temp_email AS (
	SELECT list_date_02.created_at_id as date_id,
	emails.merchant_id as merchant_uuid,
	merchant_profiles.id as merchant_profile_id,
	count(distinct emails.id) as emails
	FROM prod.emails
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', LEFT(emails.sent_at, 19)::timestamp)::date
	INNER JOIN prod.merchant_profiles
	ON merchant_profiles.uuid = emails.merchant_id
	WHERE emails.sent_at NOTNULL
	AND emails.merchant_id NOTNULL
	GROUP BY date_id, merchant_uuid, merchant_profile_id
);

DROP TABLE IF EXISTS temp_stripe_charges;
CREATE TEMP TABLE temp_stripe_charges AS (
	SELECT list_date_02.created_at_id as date_id,
	charges.merchant_id as merchant_uuid,
	merchant_profiles.id as merchant_profile_id,
	count(distinct charges.stripe_charge_id) as online_payments,
	sum(charges.amount)/100::numeric as amount
	FROM prod.charges
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', charges.created)::date
	INNER JOIN prod.merchant_profiles
	ON merchant_profiles.uuid = charges.merchant_id
	WHERE charges.status = 'succeeded'
	AND charges.stripe_charge_id NOTNULL
	GROUP BY date_id, merchant_uuid, merchant_profile_id
);

DROP TABLE IF EXISTS temp_gastrofix_charges;
CREATE TEMP TABLE temp_gastrofix_charges AS (
	SELECT list_date_02.created_at_id as date_id,
	charges.merchant_id as merchant_uuid,
	merchant_profiles.id as merchant_profile_id,
	count(distinct charges.gastrofix_charge_id) as gastrofix_payments,
	sum(charges.amount)/100::numeric as amount
	FROM prod.charges
	INNER JOIN dmart.list_date_02
	ON list_date_02.date = date_trunc('day', charges.created)::date
	INNER JOIN prod.merchant_profiles
	ON merchant_profiles.uuid = charges.merchant_id
	WHERE charges.status = 'succeeded'
	AND charges.gastrofix_charge_id NOTNULL
	GROUP BY date_id, merchant_uuid, merchant_profile_id
);


DROP TABLE IF EXISTS temp_fact_growth01_basis;
CREATE TEMP TABLE temp_fact_growth01_basis AS (
	select  a.merchant_profile_id, b.date, b.created_at_id as date_id
	from dmart.list_sfdc_accounts a
	cross join dmart.list_date_02 b
);

/**
Use the above created list and temp tables to create fact table and indices
*/
DROP TABLE IF EXISTS dmart.fact_growth_general; 
CREATE TABLE dmart.fact_growth_general AS (
SELECT temp_fact_growth01_basis.date_id, 
temp_fact_growth01_basis.merchant_profile_id,
list_sfdc_accounts.city_id,
list_sfdc_accounts.industry_id,
list_sfdc_accounts.subscription_status_id,
list_sfdc_accounts.subscription_channel_id,
list_sfdc_accounts.subscription_start_id,
list_sfdc_accounts.subscription_end_id,
agg_resources.resource_count as number_resources,
agg_services.service_count as number_services,
temp_bookings.bookings,
temp_sma.sma,
temp_feedbacks.feedbacks,
temp_messages.messages,
temp_messages.conversations, 
temp_shifts.shifts,
temp_newsletters.newsletters,
temp_newsletters.recipients as newsletter_recipients,
temp_stripe_charges.online_payments as booking_widget_payments,
temp_stripe_charges.amount as booking_widget_payment_amount,
temp_gastrofix_charges.gastrofix_payments,
temp_gastrofix_charges.amount as gastrofix_payment_amount,
temp_email.emails as emails_sent,
temp_sms.sms as sms_sent
FROM temp_fact_growth01_basis
LEFT JOIN dmart.list_sfdc_accounts
ON list_sfdc_accounts.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id
LEFT JOIN agg_resources
ON agg_resources.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id
LEFT JOIN agg_services
ON agg_services.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id
LEFT JOIN temp_bookings
ON temp_bookings.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_bookings.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_sma
ON temp_sma.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_sma.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_feedbacks
ON temp_feedbacks.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_feedbacks.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_messages
ON temp_messages.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_messages.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_shifts
ON temp_shifts.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_shifts.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_newsletters
ON temp_newsletters.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_newsletters.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_stripe_charges
ON temp_stripe_charges.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_stripe_charges.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_gastrofix_charges
ON temp_gastrofix_charges.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_gastrofix_charges.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_email
ON temp_email.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_email.date_id = temp_fact_growth01_basis.date_id
LEFT JOIN temp_sms
ON temp_sms.merchant_profile_id = temp_fact_growth01_basis.merchant_profile_id 
AND temp_sms.date_id = temp_fact_growth01_basis.date_id
);

CREATE INDEX fact_growth_general_merchant_profile_id_idx
  ON dmart.fact_growth_general
  USING btree
  (merchant_profile_id);

CREATE INDEX fact_growth_general_date_id_idx
  ON dmart.fact_growth_general
  USING btree
  (date_id);

CREATE INDEX fact_growth_general_subscription_start_id_idx
  ON dmart.fact_growth_general
  USING btree
  (subscription_start_id);

CREATE INDEX fact_growth_general_subscription_end_id_idx
  ON dmart.fact_growth_general
  USING btree
  (subscription_end_id);

CREATE INDEX fact_growth_general_city_id_idx
  ON dmart.fact_growth_general
  USING btree
  (city_id);

CREATE INDEX fact_growth_general_subscription_channel_id_idx
  ON dmart.fact_growth_general
  USING btree
  (subscription_channel_id);

DELETE FROM dmart.fact_growth_general WHERE bookings IS NULL 
AND sma IS NULL 
AND feedbacks IS NULL
and messages is null
and conversations  is null
and shifts is null
and newsletters is null
and newsletter_recipients is null
and booking_widget_payments is null
and booking_widget_payment_amount is null
and gastrofix_payments is null
and gastrofix_payment_amount is null
and emails_sent is null
and sms_sent is null;