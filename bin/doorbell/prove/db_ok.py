#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
import time
import os  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
button = 5  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
def my_callback(channel):  
	print ("Rising edge detected ")  
        os.system("mpg123 /home/rf/bin/doorbell/TrainBell.mp3 &")
	time.sleep(0.05)
	GPIO.remove_event_detect(button)
	time.sleep(0.05)
	ch=GPIO.wait_for_edge(button, GPIO.FALLING, timeout =3000 )
	time.sleep(0.05)
	if ch is None:
		print ("dopo  3s  non ancora rilasciato eseguo script nascosto")
		os.system("pppp")
		print ("aspetto ancora rilascio ")
		GPIO.wait_for_edge(button, GPIO.FALLING)
		time.sleep(0.05)

	print ("falling edge") 
        GPIO.remove_event_detect(button)
	time.sleep(0.05)
	GPIO.add_event_detect(button, GPIO.RISING, callback=my_callback, bouncetime =200)

  
GPIO.add_event_detect(button, GPIO.RISING, callback=my_callback, bouncetime =200)  

while True :
	print ("aspetto")
	time.sleep(60)

