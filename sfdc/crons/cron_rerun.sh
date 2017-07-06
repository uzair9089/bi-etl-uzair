#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/sfdc/re-run.py comm  >> /tmp/log_rerun2$$.log 2>&1
mailx -s "ETL Self Healing Status" bi-etl@shore.com  < /tmp/log_rerun2$$.log
cat /tmp/log_rerun2$$.log >> /opt/etl/core/logs/log_rerun2.txt
rm /tmp/log_rerun2$$.log
