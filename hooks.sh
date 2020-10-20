#!/bin/bash

workdir="/home/`whoami`/.config/polybar/scripts/polybar-quotation"
bar_name=`jq ".bar_name" $workdir/conf.json`
bar_name=`echo $bar_name | cut -c2-$((${#bar_name}-1))`


if [ $1 = "1" ]; then

	$workdir/quot.py --next-line
	polybar-msg -p `pgrep -f "polybar $bar_name"` hook quotation 1

elif [ $1 = "2" ]; then
	polybar-msg -p "$(pgrep -f "polybar "$bar_name)" hook quotation 2

fi
