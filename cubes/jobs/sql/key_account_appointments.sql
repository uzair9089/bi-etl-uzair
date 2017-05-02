
DROP TABLE IF EXISTS dmart.list_date;

CREATE TABLE IF NOT EXISTS dmart.list_date
(
  created_at_id serial,
  Date date,
  full_day_description text,
  day_of_week integer,
  calendar_month text,
  calendar_year integer,
  fiscal_year_month text,
  holiday text,
  weekend text,
  month_id integer
);

INSERT INTO dmart.list_date
    (
  Date,
  full_day_description,
  day_of_week ,
  calendar_month ,
  calendar_year,
  fiscal_year_month,
  holiday,
  weekend,
  month_id
    )
SELECT
    day,
    rtrim(to_char(day, 'Month')) || to_char(day, ' DD, YYYY'),

    --to_char(day, 'Day'),
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
  WHEN rtrim(to_char(day, 'Month')) = 'December' then 12 ELSE 0 END as day_of_week,

    rtrim(to_char(day, 'Month')),
    date_part('year', day),
    'F' || to_char(day, 'YYYY-MM'),
    '', --omitting (trivial 'Holiday'/'Non-Holiday, but how to get this ??),
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
  WHEN rtrim(to_char(day, 'Month')) = 'December' then 12 ELSE 0 END as month_id

FROM
    generate_series('2010-01-01'::date, current_date::date, '1 day') day;



drop table if exists dmart.list_key_accounts_account;
CREATE TABLE dmart.list_key_accounts_account AS (
  SELECT distinct Account.Id as AccountId,
      Account.dShopId__c::integer as merchant_profile_id,
      Account.Name as AccountName, 
      Account.dtotalengagementscore__c as ActivityScore,
      CASE WHEN Account.ParentId IS NULL THEN Account.Id ELSE Account.ParentId END as Parent_Id,
      '' as ParentName
    FROM prod.Account
    WHERE 
    Account.dshopid__c NOTNULL
    AND Account.RecordTypeId ='012b0000000DffCAAS' 
    AND Account.Type IN ('Trial','Customer', 'Trial Customer') 
    AND Account.ParentID NOT IN ('001b000003MxhU1','001b000000n1jFzAAI', '001b000001EjTYiAAN', '001b000000QbJBeAAN'));

    
ALTER TABLE dmart.list_key_accounts_account ADD PRIMARY KEY (accountid);

-- always use small case for naming the columns
UPDATE
    dmart.list_key_accounts_account a
SET
    parentname = aa.name
FROM prod.account aa
WHERE aa.id = a.parent_id;

DROP TABLE if exists dmart.list_widget_in_date;
CREATE TABLE dmart.list_widget_in_date as select * from dmart.list_date;

DROP TABLE if exists dmart.event_did_not_appear;
CREATE TABLE dmart.event_did_not_appear as (
  SELECT appointment_id, max(created_at) as event_created_at
  FROM prod.events
  WHERE events.type = 'Event::CustomerDidNotAppear'
  GROUP BY appointment_id ORDER BY appointment_id);

DROP TABLE IF EXISTS dmart.list_state;
CREATE TABLE IF NOT EXISTS dmart.list_state (
	id  SERIAL PRIMARY KEY,
	state VARCHAR(500)
);
INSERT INTO dmart.list_state(
	state
)
SELECT
DISTINCT
	a.state
FROM
	stage.s_appointment_series a
LEFT JOIN
	dmart.list_state b
ON
	a.state = b.state
WHERE
	b.state is NULL;


CREATE INDEX event_did_not_appear_idx
  ON dmart.event_did_not_appear
  USING btree
  (appointment_id);
  

DROP TABLE if exists dmart.given_feedbacks;
CREATE TABLE dmart.given_feedbacks as (
  SELECT appointment_id, id, updated_at, merchant_customer_id, positive
  FROM prod.feedbacks
  WHERE state = 'given');

alter table dmart.given_feedbacks add positive_bkp varchar(200);

update dmart.given_feedbacks set positive_bkp = 'Positive Feedbacks' where positive=true;

update dmart.given_feedbacks set positive_bkp = 'Negative Feedbacks' where positive=false;

alter table dmart.given_feedbacks drop column positive;

alter table dmart.given_feedbacks rename column positive_bkp TO positive;
  
CREATE INDEX given_feedbacks_id_index ON dmart.given_feedbacks USING btree (id);
CREATE INDEX given_feedbacks_appointment_id_index ON dmart.given_feedbacks USING btree (appointment_id);


DROP TABLE IF EXISTS dmart.list_created_by_merchant;
CREATE TABLE if not exists dmart.list_created_by_merchant (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);
INSERT INTO dmart.list_created_by_merchant(
	description
)
SELECT
	('SMA');
INSERT INTO dmart.list_created_by_merchant(
	description
)
SELECT
	('Booking');

DROP TABLE IF EXISTS dmart.fact_key_accounts_appointments;
CREATE TABLE dmart.fact_key_accounts_appointments AS (
SELECT 
  act.merchant_profile_id::integer, 
  list_widget_in_date.created_at_id as date_widget_in_id, 
  list_date.created_at_id as apt_created_at_id,
  extract(hour from appointment_series.created_at) as hour_id, 
  given_feedbacks.id as feedback_id,
  1 as apt_cnt,
  case when appointment_series.created_by_merchant = True then 1 else 2 end as created_by_merchant_id,
  CASE WHEN event_did_not_appear.event_created_at NOTNULL THEN 1 ELSE 0 END as No_Show, 
  list_state.id as state_id,
  CASE WHEN given_feedbacks.id NOTNULL THEN 1 ELSE 0 END as given_feedbacks
FROM prod.appointment_series
INNER JOIN dmart.list_key_accounts_account act
  ON appointment_series.merchant_profile_id = act.merchant_profile_id
LEFT JOIN dmart.event_did_not_appear --new table 1:1
  ON event_did_not_appear.appointment_id = appointment_series.uuid
LEFT JOIN prod.Account as account
  ON appointment_series.merchant_profile_id = account.dshopid__c
LEFT JOIN dmart.given_feedbacks
  ON given_feedbacks.appointment_id = appointment_series.uuid
LEFT JOIN dmart.list_date
  ON list_date.date::date = appointment_series.created_at::date
LEFT JOIN dmart.list_widget_in_date
  ON list_widget_in_date.date::date = account.dateWidgetIn__c::date
LEFT JOIN dmart.list_state
  ON list_state.state = appointment_series.state);
