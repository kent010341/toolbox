#!/bin/bash

# the color will change to red if the days of time interval
# is greater than this value 
alert_days=90

# ===========================================
# get timestamp of last password changing time
user=$(whoami)
update_timestamp=$(dscl . read /Users/"$user" | \
    grep -A1 passwordLastSetTime | grep real | \
    awk -F'real>|</real' '{print $2}')

# transfer timestamp to readable foramt
format_date=$(date -j -f %s "$update_timestamp" +"%Y/%m/%d %H:%M:%S" 2> /dev/null)

echo "The last time the password changed was:"
echo -e "\033[1;96m$format_date \033[0m"

# ===========================================
# get timestamp of current time
current_date=$(date +%s)

# floor the $update_timestamp
update_timestamp=$(echo "$update_timestamp" | cut -d"." -f 1)
# calculate time interval
time_interval=$(expr $current_date \- $update_timestamp)

seconds=$(expr $time_interval \% 60)
minutes=$(expr $time_interval \/ 60 \% 60)
hours=$(expr $time_interval \/ 3600 \% 24)
days=$(expr $time_interval \/ 86400)

# Check if time_interval is greater than the limit
echo ""
echo "Since the last change, it has been: (shouldn't be more than $alert_days days)"
if [ $time_interval -gt $(expr $alert_days \* 86400) ]; then
    # Exceeding the limit
    echo -e "\033[1;91m$days days $hours hours $minutes minutes $seconds seconds \033[0m"
    echo -e "\033[1;91mPlease change your password immediately. \033[0m"
else
    # not exceeding the limit
    echo -e "\033[1;93m$days days $hours hours $minutes minutes $seconds seconds \033[0m"
    echo ""
    echo "The password will expire at the following times:"

    limit_timestamp=$(expr $update_timestamp \+ $(expr $alert_days \* 86400))
    format_limit=$(date -j -f %s "$limit_timestamp" +"%Y/%m/%d %H:%M:%S" 2> /dev/null)
    echo -e "\033[1;93m$format_limit \033[0m"
fi
