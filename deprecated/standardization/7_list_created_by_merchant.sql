
DROP TABLE IF EXISTS dmart.list_created_by_merchant;

CREATE TABLE if not exists dmart.list_created_by_merchant (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO dmart.list_created_by_merchant(
	description
)
SELECT
	('Bookings');


INSERT INTO dmart.list_created_by_merchant(
	description
)
SELECT
	('SMA');


drop table if exists dmart.list_state_changed_by_merchant;

CREATE TABLE  if not exists dmart.list_state_changed_by_merchant (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO dmart.list_state_changed_by_merchant(
	description
)
SELECT
	('state changed by merchant');


INSERT INTO dmart.list_state_changed_by_merchant(
	description
)
SELECT
	('other');


drop table if exists dmart.list_participating_accounts;

CREATE TABLE  if not exists  dmart.list_participating_accounts (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO dmart.list_participating_accounts(
	description
)
SELECT
	('has account participants');


INSERT INTO dmart.list_participating_accounts(
	description
)
SELECT
	('has no account participants');



drop table if exists dmart.list_type;
CREATE TABLE  if not exists  dmart.list_type (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO dmart.list_type(
	description
)
SELECT
	('Appointment');


INSERT INTO dmart.list_type(
	description
)
SELECT
	('other');


drop table if  exists dmart.customer_availability;
CREATE TABLE  if not exists  dmart.customer_availability (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO dmart.customer_availability(
	description
)
SELECT
	('customer available');


INSERT INTO dmart.customer_availability(
	description
)
SELECT
	('customer not available');


	
drop table if exists dmart.list_hour;
create table dmart.list_hour as
select '1' as hour, 1 as id
union
select '2' as hour, 2 as id
union
select '3' as hour, 3 as id
union
select '4' as hour, 4 as id
union
select '5' as hour, 5 as id
union
select '6' as hour, 6 as id
union
select '7' as hour, 7 as id
union
select '8' as hour, 8 as id
union
select '9' as hour, 9 as id
union
select '10' as hour, 10 as id
union
select '11' as hour, 11 as id
union
select '12' as hour, 12 as id
union
select '13' as hour, 13 as id
union
select '14' as hour, 14 as id
union
select '15' as hour, 15 as id
union
select '16' as hour, 16 as id
union
select '17' as hour, 17 as id
union
select '18' as hour, 18 as id
union
select '19' as hour, 19 as id
union
select '20' as hour, 20 as id
union
select '21' as hour, 21 as id
union
select '22' as hour, 22 as id
union
select '23' as hour, 23 as id
union
select '0' as hour, 0 as id
order by id;




drop table if exists dmart.list_feedbacks;
CREATE TABLE if not exists dmart.list_feedbacks (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO dmart.list_feedbacks(
	description
)
SELECT
	('Has Feedbacks');


INSERT INTO dmart.list_feedbacks(
	description
)
SELECT
	('No Feedbacks');


INSERT INTO dmart.list_feedbacks(
	description
)
SELECT
	('N/A');
