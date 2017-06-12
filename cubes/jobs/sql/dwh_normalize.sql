

--creating a temporary service tables
drop table if exists app_services;
create temp table app_services as
select 
appointment_id,
count(*) as service_count, 
array_agg(id) as service_id_array,
sum(price_cents) as revenue_amt_not_euro
from prod.appointment_services
group by appointment_id;


--creating a temporary resources tables
drop table if exists app_resources;
create temp table app_resources as
select
appointment_id,
count(*) as resource_count, 
array_agg(id) as resource_id_array 
from prod.appointment_resources
group by appointment_id;



--create an appointment table which has only non-test appointments
drop table if exists app_series;
create temp table app_series as
select
a.id,
a.uuid, 
a.merchant_profile_id,
a.created_at::date,
a.created_by_merchant,
a.origin,
a.state,
a.additional_information_archive->'subject'::text as subject,
a.merchant_customer_id
from prod.appointment_series a
inner join prod.merchant_profiles b on
a.merchant_profile_id = b.id
inner join prod.merchant_key_accounts c on
c.id = b.merchant_key_account_id
where c.test=false
group by 
a.id,
a.uuid, 
a.merchant_profile_id,
a.created_at::date,
a.created_by_merchant,
a.origin,
a.state,
a.additional_information_archive->'subject'::text ,
a.merchant_customer_id;


--create an appointment table
drop table if exists star.appointments;
create table star.appointments as
select a.*,b.*,c.resource_count, c.resource_id_array from app_series a
left join app_services b on
a.id = b.appointment_id
left join app_resources c on
c.appointment_id = a.id;

--for the appointment_series_mobile
drop table if exists app_series_mobile;
create temp table app_series_mobile as
select
a.id,
a.uuid, 
a.merchant_profile_id,
a.created_at::date,
a.created_by_merchant,
a.origin,
CASE WHEN a.origin like '%ios%' and a.origin like '%pad%' THEN 'ios_tablet'
 WHEN a.origin like '%ios%' THEN 'ios_phone'
 WHEN a.origin like '%android%' and a.origin like '%tablet%' THEN 'android_tablet'
 WHEN a.origin like '%android%' THEN 'android_phone'
ELSE 'NA' end as device,
a.state,
a.additional_information_archive->'subject'::text as subject,
a.merchant_customer_id
from prod.appointment_series a
inner join prod.merchant_profiles b on
a.merchant_profile_id = b.id
inner join prod.merchant_key_accounts c on
c.id = b.merchant_key_account_id
where c.test=false and a.origin like '%mobile%' and (a.origin like '%dienstleister%' or a.origin like '%merchant%')
group by 
a.id,
a.uuid, 
a.merchant_profile_id,
a.created_at::date,
a.created_by_merchant,
a.origin,
a.state,
a.additional_information_archive->'subject'::text,
a.merchant_customer_id;


-- create an appointment seires table
drop table if exists star.appointment_series;
create table star.appointment_series as
select a.*,b.service_count, b.service_id_array,
c.resource_count, c.resource_id_array from app_series_mobile a
left join app_services b on
a.id = b.appointment_id
left join app_resources c on
c.appointment_id = a.id;



-- fact feedback creation

drop table if exists fdbks_given;
create temp table fdbks_given AS 
SELECT ap_sr.merchant_profile_id AS merchant_profile_id,
a.created_at::date AS date,
count(1) as given
FROM prod.feedbacks a
inner JOIN star.appointments ap_sr 
ON a.appointment_id = ap_sr.uuid
and a.state='given'
group by 
ap_sr.merchant_profile_id ,
a.created_at::date ,
a.state;

drop table if exists fdbks_requested;
create temp table fdbks_requested AS 
SELECT ap_sr.merchant_profile_id AS merchant_profile_id,
a.created_at::date AS date,
count(1) as requested
FROM prod.feedbacks a
inner JOIN star.appointments ap_sr 
ON a.appointment_id = ap_sr.uuid
and a.state='requested'
group by 
ap_sr.merchant_profile_id ,
a.created_at::date ,
a.state;

drop table if exists fdbks_ignored;
create temp table fdbks_ignored AS 
SELECT ap_sr.merchant_profile_id AS merchant_profile_id,
a.created_at::date AS date,
count(1) as ignored
FROM prod.feedbacks a
inner JOIN star.appointments ap_sr 
ON a.appointment_id = ap_sr.uuid
and a.state='ignored'
group by 
ap_sr.merchant_profile_id ,
a.created_at::date ,
a.state;

drop table if exists fdbks_positive;
create temp table fdbks_positive AS 
SELECT ap_sr.merchant_profile_id AS merchant_profile_id,
a.created_at::date AS date,
count(1) as positive
FROM prod.feedbacks a
inner JOIN star.appointments ap_sr 
ON a.appointment_id = ap_sr.uuid
and a.state='given' and positive=true
group by 
ap_sr.merchant_profile_id ,
a.created_at::date ,
a.state;


drop view dmart.fact_feedbacks;

drop table if exists star.fact_feedbacks;
create table star.fact_feedbacks as
select a.*, b.given, c.ignored, d.positive
from fdbks_requested a
left join fdbks_given b
on a.merchant_profile_id = b.merchant_profile_id and
a.date = b.date
left join fdbks_ignored c
on a.merchant_profile_id = c.merchant_profile_id and
a.date = c.date
left join fdbks_positive d
on a.merchant_profile_id = d.merchant_profile_id and
a.date = d.date
;

create view dmart.fact_feedbacks as select * from star.fact_feedbacks;

-- fact appointments -- this can be replaced by the app_series table

drop table if exists total_bookings;
create temp table total_bookings as
select
a.merchant_profile_id,
a.created_at::date,
count(1) as total_bookings
from prod.appointment_series a
inner join prod.merchant_profiles b on
a.merchant_profile_id = b.id
inner join prod.merchant_key_accounts c on
c.id = b.merchant_key_account_id
where c.test=false and a.created_by_merchant=false
group by 
a.merchant_profile_id,
a.created_at::date
;

-- this can also ustilize app_series
drop table if exists appyourself_bookings;
create temp table appyourself_bookings as
select
a.merchant_profile_id,
a.created_at::date,
count(1) as appyourself_bookings
from app_series a 
where a.created_by_merchant=false and origin='appyourself'
group by 
a.merchant_profile_id,
a.created_at::date
; --8331



drop table if exists inner_query;
create temp table inner_query as
SELECT count(id) as count, merchant_profile_id, created_at from app_series WHERE origin like '%mobile%' and (origin like '%dienstleister%' or 
	origin like '%merchant%') and created_by_merchant = false
	group by merchant_profile_id, created_at;

drop table if exists outer_query;
create temp table outer_query as
select count(id) as count, merchant_profile_id,created_at from app_series 
where created_by_merchant = true
group by created_at, merchant_profile_id;

drop table if exists total_sma_temp;
create table total_sma_temp as
select * from inner_query
union
select * from outer_query;

drop table if exists total_sma;
create temp table total_sma as
select sum(count) as total_sma, merchant_profile_id, created_at from total_sma_temp
group by merchant_profile_id, created_at;


drop table if exists mobile_sma;
create temp table mobile_sma as
select created_at, merchant_profile_id, count(1) as mobile_sma from app_series WHERE origin like '%mobile%' and (origin like '%dienstleister%' or origin like '%merchant%')
group by created_at,merchant_profile_id
;


-- quality sma
drop table if exists quality_sma_temp;
create temp table quality_sma_temp as
SELECT 1 as  quality_sma, created_at , merchant_profile_id
FROM star.appointments
where (CASE WHEN service_count > 0 THEN 1 ELSE 0 END
+ CASE WHEN resource_count > 0 THEN 1 ELSE 0 END
+ CASE WHEN merchant_customer_id NOTNULL THEN 1 ELSE 0 END
+ CASE WHEN subject NOTNULL OR subject != '' OR subject != ' ' THEN 1 ELSE 0 END) > 2  and created_by_merchant = true
group by created_at, merchant_profile_id,id;




drop table if exists quality_sma;
create temp table quality_sma as
select sum(quality_sma)  as quality_sma , merchant_profile_id, created_at from quality_sma_temp
group by merchant_profile_id, created_at;



drop table if exists total_revenue_eur;
create temp table total_revenue_eur as
select merchant_profile_id, created_at, sum(revenue_amt_not_euro) as revenue_amt_not_euro from star.appointments
group by merchant_profile_id, created_at;



drop table if exists customer_apmts;
create temp table customer_apmts as
select count(1) as customer_apmts, merchant_profile_id, created_at from app_series
where merchant_customer_id is not null
group by merchant_profile_id, created_at;



drop table if exists courses;
create temp table courses as
select count(1) as courses,a.created_at::date, a.merchant_profile_id 
from prod.appointment_series a
inner join prod.merchant_profiles b on
a.merchant_profile_id = b.id
inner join prod.merchant_key_accounts c on
c.id = b.merchant_key_account_id
where c.test=false and a.created_by_merchant=false and a.type = 'AppointmentGroup' or a.appointment_group_id NOTNULL
group by 
a.merchant_profile_id,
a.created_at::date;


drop table if exists no_shows;
create temp table no_shows as
select  count(1) as no_shows, apmt.created_at::date, apmt.merchant_profile_id 
FROM app_series apmt 
LEFT JOIN 
(select * from (select *,row_number() over (partition by appointment_id,created_at order by created_at desc) 
as rnk from prod.events) as t where rnk=1) 
--prod.events 
events 
ON events.appointment_id = apmt.uuid WHERE events.type = 'Event::CustomerDidNotAppear'
group by apmt.created_at::date,apmt.merchant_profile_id;



drop table if exists cancelled;
create temp table cancelled 
as select count(1) as cancelled, created_at,merchant_profile_id from app_series
where state='cancelled'
group by created_at, merchant_profile_id ;

drop table if exists deleted;
create temp table deleted as
select count(1) as deleted, a.created_at, a.merchant_profile_id from prod.appointment_series a
inner join prod.merchant_profiles b on
a.merchant_profile_id = b.id
inner join prod.merchant_key_accounts c on
c.id = b.merchant_key_account_id
where c.test=false and a.deleted_at is not null
group by a.created_at,a.merchant_profile_id;


drop view dmart.fact_appointments;



drop table if exists fact_appointments;
create  temp table fact_appointments as
select a.merchant_profile_id,
a.created_at,
d.total_bookings,
e.appyourself_bookings,
f.total_sma,
g.mobile_sma,
h.quality_sma,
i.revenue_amt_not_euro,
j.customer_apmts,
k.courses,
l.no_shows
from app_series a
left join total_bookings d on 
d.created_at = a.created_at and d.merchant_profile_id = a.merchant_profile_id
left join appyourself_bookings e
on e.created_at=a.created_at and e.merchant_profile_id= a.merchant_profile_id
left join total_sma f
on f.created_at = a.created_at and f.merchant_profile_id = a.merchant_profile_id
left join mobile_sma g 
on g.created_at = a.created_at and g.merchant_profile_id = a.merchant_profile_id
left join quality_sma h 
on h.created_at = a.created_at and h.merchant_profile_id = a.merchant_profile_id
left join total_revenue_eur i 
on i.created_at = a.created_at and i.merchant_profile_id = a.merchant_profile_id
left join customer_apmts j 
on j.created_at = a.created_at and j.merchant_profile_id = a.merchant_profile_id
left join courses k
on k.created_at = a.created_at and k.merchant_profile_id = a.merchant_profile_id
left join no_shows l
on l.created_at = a.created_at and l.merchant_profile_id = a.merchant_profile_id
;





drop table if exists star.fact_appointments;
create table star.fact_appointments as
(select * from (select *,row_number() over (partition by merchant_profile_id,created_at order by created_at desc) 
as rnk from fact_appointments) as t where rnk=1) 
;

create view dmart.fact_appointments as select * from star.fact_appointments;

GRANT SELECT ON TABLE dmart.fact_feedbacks TO dmart_user;
GRANT SELECT ON TABLE dmart.fact_appointments TO dmart_user;

--select * from star.fact_appointments order by merchant_profile_id desc limit 1000


--select count(distinct merchant_profile_id::text||created_at::text) from star.fact_appointments;

