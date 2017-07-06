#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/core/runner.py pymt  >> /tmp/log_pymt$$.log 2>&1
mailx -s "ETL Status - Payment" bi-etl@shore.com  < /tmp/log_pymt$$.log
cat /tmp/log_pymt$$.log >> /opt/etl/core/logs/log_pymt.txt
rm /tmp/log_pymt$$.log
