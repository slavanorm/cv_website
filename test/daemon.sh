#!/bin/sh

while true; do
	str=''
	if [ $(./check_git_is_latest.sh) ]
	then
		str+="$(date)\n"
		str+="$(git checkout)"
		echo $(str) >> /home/v/cv_logs
		echo need update
	else
		echo uptodate
	fi
	sleep 60;
done
