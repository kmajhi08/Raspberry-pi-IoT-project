#!/usr/bin/python3
# here hx711 load sensor used you have to download library of hx711
import RPi.GPIO as gpio
from hx711 import HX711
import http.client as httplib
import urllib
import time
key = "DX0GDLMQH4Z6ZBIU"  # Put your API Key here

def load():

    while True:
        hx711 = HX711(dout_pin=5,pd_sck_pin=6,channel='A',gain=64)
        hx711.reset()
        measures = hx711.get_raw_data(num_measures=3)
        data="\n".join(measures)
        params = urllib.urlencode({'field1': data , 'key':key }) #put your fieldnumber here
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (data)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        finally:
            gpio.cleanup()
        break
if __name__ == "__main__":
        while True:
                load()