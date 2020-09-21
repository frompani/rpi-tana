#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
import time
import os  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
button = 5  
#GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(button, GPIO.IN)  
def my_callback(channel):  
	print ("state change detected ")  
	if GPIO.input(channel):
   		print('Input was HIGH')
		os.system("mpg123 /home/rf/bin/doorbell/Cuckoo.mp3 &")
	else:
		print('Input was LOW')
#	os.system("/usr/bin/amixer -c 0 -- sset PCM -5dB &")
#	time.sleep(10)
#        os.system("/usr/bin/amixer -c 0 -- sset PCM -40dB &")

GPIO.add_event_detect(button, GPIO.BOTH, callback=my_callback, bouncetime =500)

while True :
	print ("aspetto")
	time.sleep(60)

