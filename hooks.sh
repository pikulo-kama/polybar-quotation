#!/bin/bash


if [ $1 = "1" ]; then

	/home/`whoami`/.config/polybar/scripts/polybar-quotation/quot.py --next-line
	polybar-msg -p "$(pgrep -f "polybar example")" hook quotation 1

elif [ $1 = "2" ]; then
	polybar-msg -p "$(pgrep -f "polybar example")" hook quotation 2

fi
