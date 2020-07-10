#!/usr/bin/python3
from time import sleep
from urllib.request import urlopen

a = 1 #creating a varible
baseURL = 'http://api.thingspeak.com/update?api_key=WGNK6L4DMKXSRRQT&field4=' #put your key and field number
while(a < 1000):
    print (a)
    f = urlopen(baseURL +str(a))
    f.read()
    f.close()
    sleep(5)
    a += a  
print ("Program has ended")
