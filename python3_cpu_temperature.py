#!/usr/bin/python3
#this is for sending RPi cpu temperature to thingspeak
from time import sleep
from urllib.request import urlopen

#put you api key and field number here: api_key=YOUR API & fieldNUMBER=
baseURL = 'http://api.thingspeak.com/update?api_key=WGNK6L4DMKXSRRQT&field5='
try:
    for _ in range(21):
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
        print (temp)
        f = urlopen(baseURL +str(temp))
        f.read()
        f.close()
        sleep(10)
            
except:
    print("oops! check your connection")
finally:
    print ("Program has ended")
