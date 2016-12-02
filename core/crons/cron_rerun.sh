#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/core/re-run.py comm  >> /tmp/log_rerun$$.log 2>&1
mailx -s "ETL Self Healing Status" sanjiv.upadhyaya@shore.com < /tmp/log_rerun$$.log
cat /tmp/log_rerun$$.log >> /opt/etl/core/logs/log_rerun.txt
rm /tmp/log_rerun$$.log
