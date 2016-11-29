
DROP TABLE IF EXISTS dmart.list_resources;

CREATE TABLE IF NOT EXISTS dmart.list_resources (
	id  SERIAL PRIMARY KEY,
	resource_id INTEGER,
	merchant_profile_id INTEGER,
	resource_name VARCHAR(255)

);
	
INSERT INTO dmart.list_resources(
	resource_id,
	merchant_profile_id,
	resource_name	
)
SELECT
DISTINCT
	a.id,
	a.merchant_profile_id,
	a.name
FROM
	stage.s_resources a
LEFT JOIN
	dmart.list_resources b
ON
	a.id = b.resource_id
AND
	a.merchant_profile_id = b.merchant_profile_id
WHERE
	b.id is NULL;
