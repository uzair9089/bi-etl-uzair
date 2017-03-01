#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/v2_core/runner.py core  >> /tmp/log_core$$.log 2>&1
mailx -s "ETL Status - Core" sanjiv.upadhyaya@shore.com < /tmp/log_core$$.log
cat /tmp/log_core$$.log >> /opt/etl/core/logs/log_core.txt
rm /tmp/log_core$$.log