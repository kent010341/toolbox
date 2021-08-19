#!/bin/bash

# 如果時間間隔的“日”超過這個數值，字串會變成紅色
alert_days=90

# ===========================================
# 取得最近一次變更密碼時間的timestamp
user=$(whoami)
update_timestamp=$(dscl . read /Users/"$user" | \
    grep -A1 passwordLastSetTime | grep real | \
    awk -F'real>|</real' '{print $2}')

# 轉換timestamp成可閱讀的格式
format_date=$(date -j -f %s "$update_timestamp" +"%Y/%m/%d %H:%M:%S" 2> /dev/null)

echo "最近一次變更密碼的時間為："
echo -e "\033[1;96m$format_date \033[0m"

# ===========================================
# 取得當前時間的timestamp
current_date=$(date +%s)

# 將$update_timestamp對個位數做無條件捨去
update_timestamp=$(echo "$update_timestamp" | cut -d"." -f 1)
# 計算時間區間
time_interval=$(expr $current_date \- $update_timestamp)

seconds=$(expr $time_interval \% 60)
minutes=$(expr $time_interval \/ 60 \% 60)
hours=$(expr $time_interval \/ 3600 \% 24)
days=$(expr $time_interval \/ 86400)

# 判斷是否超過限制
echo ""
echo "距離上次變更 (不得大於 $alert_days 天)："
if [ $time_interval -gt $(expr $alert_days \* 86400) ]; then
    # 超過限制
    echo -e "\033[1;91m$days 天 $hours 時 $minutes 分 $seconds 秒 \033[0m"
    echo -e "\033[1;91m請立即變更密碼。 \033[0m"
else
    # 沒超過限制
    echo -e "\033[1;93m$days 天 $hours 時 $minutes 分 $seconds 秒 \033[0m"
    echo ""
    echo "密碼將於下述時間過期："

    limit_timestamp=$(expr $update_timestamp \+ $(expr $alert_days \* 86400))
    format_limit=$(date -j -f %s "$limit_timestamp" +"%Y/%m/%d %H:%M:%S" 2> /dev/null)
    echo -e "\033[1;93m$format_limit \033[0m"
fi
