#!/bin/bash

# 如果時間間隔的“日”超過這個數值，字串會變成紅色
alert_days=90

# ===========================================
# 取得最近一次變更密碼時間的timestamp
u=$(whoami)
t=$(dscl . read /Users/"$u" | \
	grep -A1 passwordLastSetTime | grep real | \
	awk -F'real>|</real' '{print $2}')

# 轉換timestamp成可閱讀的格式
format_date=$(date -j -f %s "$t" 2> /dev/null)

echo "最近一次變更密碼的時間為："
echo -e "\033[1;96m$format_date \033[0m"

# ===========================================
# 取得當前時間的timestamp
current_date=$(date +%s)

# 將$t對個位數做無條件捨去
t=$(echo "$t" | cut -d"." -f 1)
# 計算時間區間
time_interval=$(expr $current_date \- $t)

seconds=$(expr $time_interval \% 60)
minutes=$(expr $time_interval \/ 60 \% 60)
hours=$(expr $time_interval \/ 3600 \% 24)
days=$(expr $time_interval \/ 86400)

# 判斷是否超過限制，超過的話設定為紅色，反之為黃色
if [ $time_interval -gt $(expr $alert_days \* 86400) ]; then
	# 紅色
	color="91m"
else
	# 黃色
	color="93m"
fi

echo ""
echo "距離上次變更 (不得大於 $alert_days 天)："
echo -e "\033[1;$color$days 天 $hours 時 $minutes 分 $seconds 秒 \033[0m"
