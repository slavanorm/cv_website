#!/bin/sh

while true; do
	str=''
	if [ $(./check_git_is_latest.sh) ]
	then
		str+="$(date)\n" >> /home/v/cv_logs
		str+="$(git checkout)"
		echo $(str) >> /home/v/cv_logs
	else
		echo uptodate
	fi
	sleep 60;
done
