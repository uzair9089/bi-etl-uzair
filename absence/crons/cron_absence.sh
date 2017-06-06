#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/absence/runner.py absence  >> /tmp/log_mongo_absence$$.log 2>&1
mailx -s "ETL Status - absence.io company data" sanjiv.upadhyaya@shore.com < /tmp/log_mongo_absence$$.log
cat /tmp/log_mongo_absence$$.log >> /opt/etl/absence/logs/log_mongo_absence .txt