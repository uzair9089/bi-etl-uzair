#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/mongo_cs/runner.py cs  >> /tmp/log_mongo_cs$$.log 2>&1
mailx -s "ETL Status - customer service mongo" sanjiv.upadhyaya@shore.com < /tmp/log_mongo_cs$$.log
cat /tmp/log_mongo_cs$$.log >> /opt/etl/mongo_cs/logs/log_mongo_cs.txt