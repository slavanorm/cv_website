#!/bin/sh

while true; do
	git fetch
	check=$(git status | grep "up to date" | wc -l)
	if [ check==0 ]
	then
		str="updating $(date +%H:%M_%m-%d-%y)"
		echo $str >> /home/v/cv_website/bash/../../cv_logs
		echo $(git status) >> /home/v/cv_website/bash/../../cv_logs
		git pull
		python3 /home/v/cv_website/bash/../main.py
	fi
	sleep 60;
done
