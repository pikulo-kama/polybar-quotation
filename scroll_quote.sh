#!/bin/bash

workdir="/home/`whoami`/.config/polybar/scripts/polybar-quotation"
line_len=$(jq ".line_max_length" $workdir/conf.json)


zscroll -l $line_len \
	--delay 0.1 \
	--match-command $workdir"/quot.py --status" \
	--match-text "PLAY" "--scroll 1" \
	--match-text "PAUSE" "--scroll 0" \
	--update-check true $workdir'/quot.py --full-quote' &
wait
