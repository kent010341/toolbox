#!/bin/bash

# the color will change to red if the days of time interval
# is greater than this value 
alert_days=90

# ===========================================
# get timestamp of last password changing time
u=$(whoami)
t=$(dscl . read /Users/"$u" | \
	grep -A1 passwordLastSetTime | grep real | \
	awk -F'real>|</real' '{print $2}')

# transfer timestamp to readable foramt
format_date=$(date -j -f %s "$t" 2> /dev/null)

echo "The last time the password changed was:"
echo -e "\033[1;96m$format_date \033[0m"

# ===========================================
# get timestamp of current time
current_date=$(date +%s)

# floor the $t
t=$(echo "$t" | cut -d"." -f 1)
# calculate time interval
time_interval=$(expr $current_date \- $t)

seconds=$(expr $time_interval \% 60)
minutes=$(expr $time_interval \/ 60 \% 60)
hours=$(expr $time_interval \/ 3600 \% 24)
days=$(expr $time_interval \/ 86400)

# color
if [ $time_interval -gt $(expr $alert_days \* 86400) ]; then
	# red
	color="91m"
else
	# yellow
	color="93m"
fi

echo ""
echo "Since the last change, it has been: (shouldn't be more than $alert_days days)"
echo -e "\033[1;$color$days d $hours h $minutes m $seconds s \033[0m"
