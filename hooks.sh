#!/bin/bash

bar_name="example"

if [ $1 = "1" ]; then

	/home/`whoami`/.config/polybar/scripts/polybar-quotation/quot.py --next-line
	polybar-msg -p "$(pgrep -f "polybar "$bar_name)" hook quotation 1

elif [ $1 = "2" ]; then
	polybar-msg -p "$(pgrep -f "polybar "$bar_name)" hook quotation 2

fi
