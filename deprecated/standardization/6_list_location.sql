
DROP TABLE IF EXISTS dmart.list_location;

CREATE TABLE IF NOT EXISTS dmart.list_location (
	id  SERIAL PRIMARY KEY,
	address_city VARCHAR(500),
	address_country_code VARCHAR(100)

);

INSERT INTO dmart.list_location(
	address_city,
	address_country_code
)
SELECT
DISTINCT
	a.address_city,
	a.address_country_code
FROM
	stage.s_appointment_series a
LEFT JOIN
	dmart.list_location b
ON
	a.address_city = b.address_city
AND
	a.address_country_code = b.address_country_code
WHERE
	b.id is NULL
AND
	a.address_city is not null 
AND
	a.address_country_code is not null;



INSERT into dmart.list_location(id,address_city, address_country_code)
	SELECT 0 as id, 'N/A' as address_city, 'N/A' as address_country_code;
