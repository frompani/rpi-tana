#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
#OK a tavolino.. quando messo sul campo dava i numeri!!
 
import time
import os  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
button = 5  
button2 = 6
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
##GPIO.setup(button, GPIO.IN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
def my_callback(channel):  
	print ("Rising edge detected ")  
#	os.system("/usr/bin/amixer -c 0 -- sset PCM -5dB &")
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
#        os.system("/usr/bin/amixer -c 0 -- sset PCM -40dB &")


def my_callback2(channel):
        print ("Rising edge detected ")
        os.system("mpg123 /home/rf/bin/doorbell/TrainBell.mp3 &")
        time.sleep(0.05)
        GPIO.remove_event_detect(button2)
        time.sleep(0.05)
        ch=GPIO.wait_for_edge(button2, GPIO.FALLING, timeout =3000 )
        time.sleep(0.05)
        if ch is None:
                print ("dopo  3s  non ancora rilasciato eseguo script nascosto")
                os.system("pppp")
                print ("aspetto ancora rilascio ")
                GPIO.wait_for_edge(button2, GPIO.FALLING)
                time.sleep(0.05)

        print ("falling edge")
        GPIO.remove_event_detect(button2)
        time.sleep(0.05)
        GPIO.add_event_detect(button2, GPIO.RISING, callback=my_callback, bouncetime =200)


GPIO.add_event_detect(button, GPIO.RISING, callback=my_callback, bouncetime =500)  
GPIO.add_event_detect(button2, GPIO.RISING, callback=my_callback2, bouncetime =200)

while True :
	print ("aspetto")
	time.sleep(60)

