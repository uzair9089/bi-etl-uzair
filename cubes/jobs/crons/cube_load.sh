#!/bin/sh
source /opt/credential/pass.sh && python /opt/etl/cubes/jobs/main.py  >> /tmp/cube_load$$.log 2>&1
mailx -s "Daily Cube Load" bi-etl@shore.com  < /tmp/cube_load$$.log
cat /tmp/cube_load$$.log >> /opt/etl/cubes/jobs/logs/cube_load.txt
rm /tmp/cube_load$$.log
