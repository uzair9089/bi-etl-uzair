#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/v2_core/runner.py msg  >> /tmp/log_msg$$.log 2>&1
mailx -s "ETL Status - Messages" sanjiv.upadhyaya@shore.com < /tmp/log_msg$$.log
cat /tmp/log_msg$$.log >> /opt/etl/core/logs/log_msg.txt
rm /tmp/log_msg$$.log
