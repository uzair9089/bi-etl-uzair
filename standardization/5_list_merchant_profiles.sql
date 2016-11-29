
DROP TABLE IF EXISTS dmart.list_merchant_profiles;

CREATE TABLE IF NOT EXISTS dmart.list_merchant_profiles (
	id  SERIAL PRIMARY KEY,
	merchant_profile_id INTEGER,
	merchant_created_at_id INTEGER,
	uuid uuid,
	name VARCHAR(255),
	expertise VARCHAR(200),
	street VARCHAR(255),
	country_code VARCHAR(50),
	city VARCHAR(255),
	has_website integer,
	has_social_media integer,
	merchant_age varchar(250)
);

INSERT INTO dmart.list_merchant_profiles(
	merchant_profile_id,
	merchant_created_at_id,
	uuid,
	name,
	expertise,
	street,
	country_code,
	city,
	has_website,
	has_social_media,
	merchant_age
)
SELECT
DISTINCT
	a.id,
	merchant_created_date.created_at_id,
	a.uuid,
	a.name,
	a.main_category_slug,
	a.street,
	a.address_country,
	a.city_slug,
	case when length(a.website) >1 then 1 else 0 end as website,
	case when a.social_media_links <> '{}' then 1 else 0 end as social_media_links,
	case when current_date::date - a.created_at::date >= 0 and current_date::date - a.created_at::date < 365 then '1 yr'
		when current_date::date - a.created_at::date >= 365 and current_date::date - a.created_at::date < 730 then '2 yrs' 
		when current_date::date - a.created_at::date >= 730 and current_date::date - a.created_at::date < 1095 then '3 yrs'
		when current_date::date - a.created_at::date >= 1095 and current_date::date - a.created_at::date <1460  then '4 yrs'
		when current_date::date - a.created_at::date >= 1460 and current_date::date - a.created_at::date <1825  then '5 yrs'
		when current_date::date - a.created_at::date >= 1825 and current_date::date - a.created_at::date <2190  then '6 yrs'
		ELSE 'N/A' END

FROM
	stage.s_merchant_profiles a
LEFT JOIN
	dmart.list_merchant_profiles b
ON
	a.id = b.merchant_profile_id

LEFT JOIN
	dmart.list_merchant_created_date merchant_created_date
ON 
	merchant_created_date.date= a.created_at::date

WHERE
	b.id is NULL;
