
DROP TABLE IF EXISTS dmart.list_services;

CREATE TABLE IF NOT EXISTS dmart.list_services (
	id  SERIAL PRIMARY KEY,
	service_id INTEGER,
	merchant_profile_id VARCHAR(255),
	service_name VARCHAR(255)

);

INSERT INTO dmart.list_services(
	service_id,
	merchant_profile_id,
	service_name	
)
SELECT
DISTINCT
	a.id,
	a.merchant_profile_id,
	a.name
FROM
	stage.s_services a
LEFT JOIN
	dmart.list_services b
ON
	a.id = b.service_id
WHERE
	b.service_id is NULL;
