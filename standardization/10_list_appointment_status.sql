

DROP TABLE IF EXISTS dmart.list_appointment_status;

CREATE TABLE dmart.list_appointment_status (
	id SERIAL PRIMARY KEY,
	cancelled VARCHAR(255)
);

INSERT INTO dmart.list_appointment_status(
	cancelled
)
SELECT
	('Appointment Cancelled');


INSERT INTO dmart.list_appointment_status(
	cancelled
)
SELECT
	('Appointment Active');