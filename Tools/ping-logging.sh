#!/bin/bash

# default
period=3 #s
target="google.com"

while (($#)); do
    case $1 in
        "--period" | "-p")
            shift
            period=$1
            shift
        ;;
        "--target" | "-t")
            shift
            target=$1
            shift
        ;;
        "--help" | "-h")
            echo "Usage: ./ping-logging.sh [options...]"
            echo "    --period <period>, -p <period>"    
            echo "        period (in second) between each pings (default: 3)"
            echo "    --target <target ip/url>, -t <target ip/url>"
            echo "        ping target (default: google.com)"
            exit 1
        ;;
        *)
            echo "unknown argument '$1'"
            echo "Use --help (or -h) to get the usage information."
            exit 1
        ;;
    esac
done

echo -e "\033[1;96mProcess Start \033[0m"
log_filename=ping_$(date +"%Y%m%d-%H%M%S").log

while true; do
    output=$(ping $target -c 1)
    curr_time=$(date +"%Y/%m/%d %H:%M:%S")

    if [ "$(echo $output | grep "100.0% packet loss")" != "" ]; then
        echo -e "\033[1;91m[$curr_time] Ping $target failed. \033[0m"
    fi
    echo "[$curr_time]\n$output\n" >> log_filename

    sleep "$period"s
done
