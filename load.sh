# export LOAD=`cat /proc/loadavg | cut -c1-14` && export UPTIME=$((`cat /proc/uptime | cut -d. -f1`)) && export FINAL="$LOAD,$UPTIME"
# echo $FINAL > /home/obsat/load/$EPOCHSECONDS.csv
