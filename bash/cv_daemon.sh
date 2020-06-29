#!/bin/sh

while true; do
	check=$(git status | grep "up to date" | wc -l)
	if [ check==1 ]
	then
		str="updating $(date +%H:%M_%m-%d-%y)"
		echo $str >> ../../cv_logs
		git pull
		python3 ../main.py
	fi
	sleep 60;
done
