#!/bin/sh
NOW=$(date +"%Y-%m-%d")
NAME="RPI-Domoticz"
SOURCE="/home/pi/"
DESTINATION="/media/removable/raid/backup/domoticz_bkp"
LOGFILE=/media/removable/raid/backup/domoticz_bkp/log/$NAME.$NOW.txt
echo  ------------------- START $NAME -- $(date +"%Y-%m-%d %H:%M:%S") | tee -a $LOGFILE
rsync -aP --stats --delete-after --links --link-dest="$DESTINATION/__prev/" "$SOURCE" "$DESTINATION/$NOW" | tee -a $LOGFILE
rm -f "$DESTINATION/__prev"
ln -s "$NOW" "$DESTINATION/__prev"
echo  ------------------- END  $NAME -- $(date +"%Y-%m-%d %H:%M:%S") | tee -a $LOGFILE
