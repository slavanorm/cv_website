#!/bin/sh
$(git fetch)
Test=$(git status | grep "up to date" | wc -l)
ret=1

if [ $Test = 1 ]; then
	ret=0
	echo $Test
fi
exit $ret
