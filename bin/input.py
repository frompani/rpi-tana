import os
import logging
from gpiozero import Button 
from signal import pause
######
###ATTENZIONE: lo script deve essere riavviato daily se no non funziona bene (perde dei segnali
##############################################
#inizializzo il logging
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
LOG_FILE = '/home/pi/log/input.log'
LOG_FORMAT = '[%(asctime)s]  [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, level=logging.DEBUG, filename=LOG_FILE)
logging.info('AVVIO')
##############################################

def gpio20_on():
    logging.info("chiuso contatto gpio20")
    print("chiuso contatto gpio20")
    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=96&switchcmd=On"')

def gpio21_on():
    logging.info("chiuso contatto gpio21")
    print("chiuso contatto gpio21")
    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=97&switchcmd=On"')

def gpio20_off():
    logging.info("aperto contatto gpio20")
    print("aperto contatto gpio20")
    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=96&switchcmd=Off"')

def gpio21_off():
    logging.info("aperto contatto gpio21")
    print("aperto contatto gpio21")
    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=97&switchcmd=Off"')

gpio20 = Button(20,pull_up=True,bounce_time=0.2)
gpio21 = Button(21,pull_up=True,bounce_time=0.2)

gpio20.when_pressed = gpio20_on
gpio21.when_pressed = gpio21_on
gpio20.when_released = gpio20_off
gpio21.when_released = gpio21_off


pause()




