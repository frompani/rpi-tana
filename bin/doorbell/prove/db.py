#!/usr/bin/env python2.7
#prova--NON funziona co versione aggiornata GPIO
import RPi.GPIO as GPIO
import time
from time import sleep
button = 5

GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time_stamp = time.time()

def my_callback(channel):
        time_stamp=time.time()
        print "rising detect"
        GPIO.remove_event_detect(button)
        GPIO.wait_for_edge(button, GPIO.FALLING)
	print ("falling detect")
        #USARE timeout nella funzione waitforedge
        time_now=time.time()
        if (time_now - time_stamp) >=3:
                print ("premuto piu di 3 s.  eseguo script")
        GPIO.add_event_detect(button, GPIO.RISING, callback=my_callback, bouncetime =100)
	print ("rimesso event detect ed esco dalla function")

raw_input ("press enter ")
GPIO.add_event_detect(button, GPIO.RISING, callback=my_callback, bouncetime=100)
try:
        sleep (11130)
finally:
        GPIO.cleanup()
