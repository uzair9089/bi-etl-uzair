#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/core/runner.py comm  >> /tmp/log_comm$$.log 2>&1
mailx -s "ETL Status - Communications" bi-etl@shore.com  < /tmp/log_comm$$.log
cat /tmp/log_comm$$.log >> /opt/etl/core/logs/log_comm.txt
rm /tmp/log_comm$$.log
