#!/usr/bin/python
#--------------------------------------
#
#              ds18b20.py
#  Read DS18B20 1-wire temperature sensor
#
# Author : Matt Hawkins
# Date   : 10/02/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()

    return int(mytemp[1])

  except:
    return 99999

if __name__ == '__main__':

  # Script has been called directly
  id = '28-80000026cc55'
  print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))
  id = '28-800000270667'
  print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))


http://192.168.10.180/tana/add_1.php?t_ext_aria=5&t_ext_muro=9
