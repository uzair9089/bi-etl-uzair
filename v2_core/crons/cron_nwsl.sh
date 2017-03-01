#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/v2_core/runner.py nwsl  >> /tmp/log_nwsl$$.log 2>&1
mailx -s "ETL Status - Newsletters" sanjiv.upadhyaya@shore.com < /tmp/log_nwsl$$.log
cat /tmp/log_nwsl$$.log >> /opt/etl/core/logs/log_nwsl.txt
rm /tmp/log_nwsl$$.log
