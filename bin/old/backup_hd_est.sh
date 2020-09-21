#/bin/sh
now=$(date)
umount /media/removable
mount /media/removable
  if [ $? != 0 ]; then
   echo "problemi nel montare il disco esterno..."
   exit
  fi
echo "montato disco USB esterno , inizio copia" $now
cd /media/removable/film
rsync -avzq --ignore-existing * /media/usb/film
echo "finito copia cartella film"
cd /media/removable/Serie-tv
rsync -avzq --ignore-existing * /media/usb/Serie-tv
echo "finito copia cartella Serie-tv"
cd /media/removable/cartoni
rsync -avzq --ignore-existing * /media/usb/cartoni
echo "finito copia cartella cartoni"



now=$(date)
echo "finito copia" $now
umount /media/removable
 if [ $? != 0 ]; then
   echo "problemi nello smontare il disco esterno..." $now
   exit
  fi
# rsync -avz * /media/usb &
