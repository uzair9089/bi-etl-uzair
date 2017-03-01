#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/v2_core/runner.py pymt  >> /tmp/log_pymt$$.log 2>&1
mailx -s "ETL Status - Payment" sanjiv.upadhyaya@shore.com < /tmp/log_pymt$$.log
cat /tmp/log_pymt$$.log >> /opt/etl/core/logs/log_pymt.txt
rm /tmp/log_pymt$$.log
