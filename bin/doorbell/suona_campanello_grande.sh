#!/bin/bash
pkill mpg123
sleep 0.1
#v=$(curl -s "http://192.168.10.181:8888/json.htm?type=devices&rid=44"|grep "Data"|rev |cut -d ":" -f1 |rev |cut -c2-3)
amixer -M sset 'PCM' 90%


#mpg123 -quiet /home/pi/bin/doorbell/mp3/lucia.mp3  > /dev/null &
mpg123 -quiet /home/pi/bin/doorbell/mp3/BELLS1.mp3  > /dev/null &
#mpg123 /home/pi/bin/doorbell/mp3/TrainBell.mp3

v=$(curl -s "http://192.168.10.181:8888/json.htm?type=devices&rid=71"|grep "Data"|rev |cut -d ":" -f1 |rev |cut -c2-3)
amixer -M sset 'PCM' $v%




