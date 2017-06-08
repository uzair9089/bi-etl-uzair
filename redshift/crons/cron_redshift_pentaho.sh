#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/redshift/runner.py pentaho >> /tmp/log_redshift_pentaho$$.log 2>&1
mailx -s "ETL Status - Redshift Migration" sanjiv.upadhyaya@shore.com < /tmp/log_redshift_pentaho$$.log
cat /tmp/log_redshift_pentaho$$.log >> /opt/etl/redshift/logs/log_redshift_pentaho.txt
rm /tmp/log_redshift_pentaho$$.log
