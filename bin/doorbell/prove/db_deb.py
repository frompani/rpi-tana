#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import os
#
led = 4
button = 5
#init GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#
i = 1
while i:
   ch1 = GPIO.wait_for_edge(button, GPIO.BOTH, bouncetime=200, timeout=5000)
   if ch1 is None:
       print('premuto nulla')
   else:
      os.system("mpg123 /root/bin/Cuckoo.mp3 &")     
      print('premuto bottone ...lancio lo script e aspetto che venga rilasciato')
      GPIO.remove_event_detect(button)
      ch2 = GPIO.wait_for_edge(button, GPIO.BOTH, bouncetime=200, timeout=5000)
      print('bottone è stato rilasciato')  
      if ch2 is None:
           print('premuto per piu di 5 s ...eseguo script nascosto....')
           os.system("script_nascosto.sh &")
   print('fine loop')
   GPIO.remove_event_detect(button)
