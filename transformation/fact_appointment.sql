
-- aggregation of the messages sent by the merchants till date

drop table if exists dmart.agg_msg_cnt;
create table dmart.agg_msg_cnt as
select a.conversation_id,a.group_id, coalesce(b.msg_cnt,0)  as msg_cnt from 
(
select distinct conversation_id,group_id from prod.participants where group_id in 
(select group_id from prod.participants
group by group_id
having count(distinct conversation_id)<2)) a 
left join (
select conversation_id, count(1) as msg_cnt from prod.messages
group by conversation_id
order by conversation_id
) b
on b.conversation_id = a.conversation_id
;


--- aggregation for appointment edits
drop table if exists dmart.agg_app_edits;
create table dmart.agg_app_edits
as 
select count(1)-1 as edits, id as appointment_series_id from prod.appointment_series 
group by id;

-- Aggregated tables
drop table if exists dmart.agg_app_rsr;
create table dmart.agg_app_rsr 
as 
select appointment_id, count(1) as rsr_nr, case when count(1) >= 0 and count(1) < 6 then '1-5' 
when count(1) >= 6 and count(1) < 11 then '6-10'
when count(1) >= 11 and count(1) < 16 then '11-15'
when count(1) >= 16 and count(1) < 21 then '16-20'
when count(1) >= 21 and count(1) < 26 then '21-25'
when count(1) >= 26 and count(1) < 31 then '26-30'
when count(1) >= 31 then 'large resource'
else 'other' end as rsr_nr_step from prod.appointment_resources
group by appointment_id;



--- Aggregation of the appointment services tables
drop table if exists dmart.agg_app_serv;
create table dmart.agg_app_serv
as 
select appointment_id, sum(price_cents) as price,count(1) as serv_nr , case when count(1) >= 0 and count(1) < 6 then '1-5' 
when count(1) >= 6 and count(1) < 11 then '6-10'
when count(1) >= 11 and count(1) < 16 then '11-15'
when count(1) >= 16 and count(1) < 21 then '16-20'
when count(1) >= 21 and count(1) < 26 then '21-25'
when count(1) >= 26 and count(1) < 31 then '26-30'
when count(1) >= 31 then 'Many services'
else 'other' end as serv_nr_step from prod.appointment_services
group by appointment_id;




DROP TABLE IF EXISTS dmart.fact_appointments;

CREATE TABLE IF NOT EXISTS dmart.fact_appointments (
	appointment_series_id INTEGER,
	merchant_profile_id integer,
	appointment_series_uuid uuid,
	created_at_id INTEGER,
	merchant_created_at_id INTEGER,
	hour_id INTEGER,
	appointment_cancelled_id INTEGER,
	bookings INTEGER,
	state_changed_by_merchant_id INTEGER,
	type_id INTEGER,
	has_customer_id INTEGER,
	churn_id INTEGER,
	origin_id INTEGER,
	price NUMERIC,
	state_id INTEGER,
	location_id INTEGER,
	feedback_id INTEGER,
	msg_cnt INTEGER,
	edit_cnt INTEGER
	
);

INSERT INTO dmart.fact_appointments(
	appointment_series_id,
	merchant_profile_id,
	appointment_series_uuid,
	created_at_id,
	merchant_created_at_id,
	hour_id,
	appointment_cancelled_id,
	bookings,
	state_changed_by_merchant_id,
	type_id,
	has_customer_id,
	churn_id,
	origin_id,
	price,
	state_id,
	location_id,
	feedback_id,
	msg_cnt,
	edit_cnt
	

)
SELECT

	app_series.id as appointment_series_id,
	app_series.merchant_profile_id as merchant_profile_id,
	app_series.uuid as appointment_series_uuid,
	list_date.created_at_id,
	list_merchant_profiles.merchant_created_at_id,
	extract( hour from app_series.created_at) as hour_id,
	case when app_series.deleted_at is not NULL then 1 ELSE 2 end as appointment_cancelled_id,
	case when app_series.created_by_merchant = True then 1 else 0 end as bookings,
	case when app_series.state_changed_by_merchant = True then 1 else 2 end as state_changed_by_merchant_id,
	case when app_series.type = 'Appointment' then 1 else 2 end as type_id,
	case when length(app_series.customer_json::text)>=1 then 1 else 2 end as has_customer_id,
	case when acct.fmlsubscriptionstatus__c = 'Active' then 1  when acct.fmlsubscriptionstatus__c ='Canceled' then 2 when acct.fmlsubscriptionstatus__c ='Terminated in Due Time' then 3  else 4 end as churn_id,
	coalesce(list_origin.id,0) as origin_id,
	coalesce(app_service.price,0),
	coalesce(list_state.id,0),
	coalesce(list_loc.id,0),
	case when feed.positive =true then 1 when feed.positive=false then 2 else 3 end as feedback_id,
	coalesce(agg_msg_cnt.msg_cnt,0) ,
	coalesce(agg_app_edits.edits,0)
FROM
	prod.appointment_series app_series
LEFT JOIN
	dmart.list_date list_date
ON
	app_series.created_at::date = list_date.Date 

LEFT JOIN
	dmart.list_origin
ON
	app_series.origin = list_origin.origin

LEFT JOIN 
	dmart.agg_app_serv app_service
 ON
 	app_service.appointment_id = app_series.id
LEFT JOIN
	prod.feedbacks feed
ON
	feed.appointment_id = app_series.uuid

LEFT JOIN 
	dmart.list_state list_state 
ON
	list_state.state = app_series.state

LEFT JOIN
	dmart.list_location list_loc
ON
	list_loc.address_country_code = app_series.address_country_code
AND
	list_loc.address_city = app_series.address_city

INNER JOIN
	prod.account acct
ON
	acct.dshopid__c = app_series.merchant_profile_id
LEFT JOIN
	dmart.agg_msg_cnt agg_msg_cnt
ON
	agg_msg_cnt.group_id = app_series.uuid
LEFT JOIN
	dmart.agg_app_edits agg_app_edits
ON
	agg_app_edits.appointment_series_id = app_series.id

LEFT JOIN
	dmart.list_merchant_profiles list_merchant_profiles
ON
	list_merchant_profiles.merchant_profile_id = app_series.merchant_profile_id
;



UPDATE
    dmart.fact_appointments a
SET
    merchant_created_at_id = aa.merchant_created_at_id
FROM dmart.list_merchant_profiles aa
WHERE aa.merchant_profile_id = a.merchant_profile_id;
