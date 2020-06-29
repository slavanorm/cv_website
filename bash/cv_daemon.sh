#!/bin/sh

while true; do
	if [ ! $(./check_git_is_latest.sh) ]
	then
		str="updating $(date +%H:%M_%m-%d-%y)"
		echo $str >> ~/cv_logs
		git pull
		python3 ../main.py
	fi
	sleep 60;
done
