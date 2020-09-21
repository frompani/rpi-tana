#!/bin/bash
amixer -M sset 'PCM' 65%
 
o=`date +%-I` 
for (( i=1; i <=$o ; i++ )) 
do 
echo $i
#omxplayer /root/bin/Cuckoo.mp3 
mpg123 /home/pi/bin/Cuckoo.mp3
done
