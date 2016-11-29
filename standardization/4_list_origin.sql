
DROP TABLE IF EXISTS dmart.list_origin;

CREATE TABLE IF NOT EXISTS dmart.list_origin (
	id  SERIAL PRIMARY KEY,
	origin VARCHAR(255)

);

INSERT INTO dmart.list_origin(
	origin
)
SELECT
DISTINCT
	a.origin
FROM
	stage.s_appointment_series a
LEFT JOIN
	dmart.list_origin b
ON
	a.origin = b.origin
WHERE
	b.origin is NULL
AND
	a.origin is not NULL;


INSERT into dmart.list_origin(id,origin)
	SELECT 0 as id, 'N/A' as origin;