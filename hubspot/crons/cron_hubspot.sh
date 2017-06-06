#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/hubspot/runner.py hubspot  >> /tmp/log_hubspot$$.log 2>&1
mailx -s "ETL Status - absence.io company data" sanjiv.upadhyaya@shore.com < /tmp/log_hubspot$$.log
cat /tmp/log_hubspot$$.log >> /opt/etl/absence/logs/log_hubspot .txt