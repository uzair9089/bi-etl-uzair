#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/redshift/runner.py star >> /tmp/log_redshift_star$$.log 2>&1
mailx -s "ETL Status - Redshift Migration" sanjiv.upadhyaya@shore.com < /tmp/log_redlog_redshift_star$$.log
cat /tmp/log_redshift_star$$.log >> /opt/etl/redshift/logs/log_redshift_star.txt
rm /tmp/log_redshift_star$$.log
