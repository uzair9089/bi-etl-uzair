#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/absenceGA/ga_runner.py >> /tmp/log_ga$$.log 2>&1
mailx -s "ETL Status - Google Analytics for absence" bi-etl@shore.com  < /tmp/log_ga$$.log
cat /tmp/log_ga$$.log >> /opt/etl/absenceGA/logs/log_ga.txt
rm /tmp/log_ga$$.log