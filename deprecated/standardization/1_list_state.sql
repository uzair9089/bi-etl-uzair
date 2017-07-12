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
