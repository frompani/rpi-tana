import RPi.GPIO as GPIO
import time
import os

def blink(channel, count = 1, timeHigh = 1000, timeLow = 1000):
    """Blink count times, timeHigh milliseconds high, timeLow milliseconds low."""

    if count <= 0:
         return
 
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(timeHigh / 1000.0)
    GPIO.output(channel, GPIO.LOW)
 
    for i in range(count - 1):
        time.sleep(timeLow / 1000.0)
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(timeHigh / 1000.0)
        GPIO.output(channel, GPIO.LOW)

led = 4
button = 5

# Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.wait_for_edge(button, GPIO.FALLING)
channel = GPIO.wait_for_edge(button, GPIO.RISING, timeout = 3000)
if channel is None:
    blink(led, 3, 500, 500)
    print "Shutdown"
    os.system("/sbin/shutdown -h now")
else:
    blink(led, 1, 500)
    print "Reboot"
    os.system("/sbin/shutdown -r now")
 
GPIO.cleanup()
