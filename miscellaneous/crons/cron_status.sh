#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/miscellaneous/notify.py >> /tmp/log_status$$.log 2>&1
mailx -s "ETL Failure Notification" sanjiv.upadhyaya@shore.com < /tmp/log_status$$.log
cat /tmp/log_status$$.log >> /opt/etl/core/logs/log_status.txt
rm /tmp/log_status$$.log
