#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/sfdc/sf_runner.py  >> /tmp/log_sfdc$$.log 2>&1
mailx -s "ETL Status - Sales Force" bi-etl@shore.com  < /tmp/log_sfdc$$.log
cat /tmp/log_sfdc$$.log >> /opt/etl/sfdc/logs/log_sfdc.txt
rm /tmp/log_sfdc$$.log
