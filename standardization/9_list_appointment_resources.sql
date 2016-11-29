

DROP TABLE IF EXISTS dmart.list_appointment_resources;

CREATE TABLE IF NOT EXISTS dmart.list_appointment_resources (
	id  SERIAL PRIMARY KEY,
	resource_id INTEGER,
	appointment_id INTEGER,
	resource_name VARCHAR(255)

);

INSERT INTO dmart.list_appointment_resources(
	resource_id,
	appointment_id,
	resource_name	
)
SELECT
DISTINCT
	a.id,
	a.appointment_id,
	a.name
FROM
	stage.s_appointment_resources a
LEFT JOIN
	dmart.list_appointment_resources b
ON
	a.id = b.resource_id
AND
	a.appointment_id = b.appointment_id
WHERE
	b.id is NULL;
