#!/bin/bash
for (( i=0; i <7 ; i++ ))
do
#gpio mode $i out
gpio write $i 1
done
sleep 1
gpio write 26 1

