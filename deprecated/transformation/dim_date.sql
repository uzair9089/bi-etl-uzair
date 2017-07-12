
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
