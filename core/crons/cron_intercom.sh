#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/v1_core/runner.py intercom  >> /tmp/log_intercom$$.log 2>&1
mailx -s "ETL Status - Intercom" bi-etl@shore.com  < /tmp/log_intercom$$.log
cat /tmp/log_intercom$$.log >> /opt/etl/core/logs/log_intercom.txt
rm /tmp/log_intercom$$.log
