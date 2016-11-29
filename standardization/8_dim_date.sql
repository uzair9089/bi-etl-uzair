DROP TABLE IF EXISTS dmart.list_date;

CREATE TABLE IF NOT EXISTS dmart.list_date
(
	created_at_id serial,
	Date date,
	full_day_description text,
	day_of_week text,
	calendar_month text,
	calendar_year integer,
	fiscal_year_month text,
	holiday text,
	weekend text 
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
	weekend 
    )
SELECT
    day,
    rtrim(to_char(day, 'Month')) || to_char(day, ' DD, YYYY'),
    to_char(day, 'Day'),
    rtrim(to_char(day, 'Month')),
    date_part('year', day),
    'F' || to_char(day, 'YYYY-MM'),
    '', --omitting (trivial 'Holiday'/'Non-Holiday, but how to get this ??),
    CASE
        WHEN date_part('isodow', day) IN (6, 7) THEN 'Weekend'
        ELSE 'Weekday'
    END
FROM
    generate_series('2010-01-01'::date, current_date::date, '1 day') day;


DROP TABLE IF EXISTS dmart.list_merchant_created_date;

CREATE TABLE dmart.list_merchant_created_date as select * from dmart.list_date;


