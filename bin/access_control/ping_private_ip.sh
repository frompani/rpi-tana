#!/bin/bash
HOSTS=$1
COUNT=2
DATE=`date +%Y-%m-%d:%H:%M:%S`
#####################################################
#####################################################
for myHost in $HOSTS
do 
 case $myHost in
        192.168.10.60 )
                name="Chiara"
        ;;
        192.168.10.61 )
                name="Fabrizio"
        ;;
 esac
 
 count=$(ping -c $COUNT $myHost | grep 'received' | awk -F',' '{ print $2 }' | awk '{ print $1 }')

  if [ $count -eq 0 ]; then
    # 100% failed 
    echo "$name NON è a casa! at $DATE"
    else 
    echo "$name è a casa at $DATE"
  fi
done
