#!/usr/bin/env python3
"""
the code is designed for collecting and sending data of pizoelectric vibration sensor using RPi
and thingspeak cloud, ADS1115 adc is used. Data is update in my channel
"""
import http.client as http 
import urllib
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0) # sensor input connected in pin0
vibration = chan.value # reading the value of senosr
key = "ABCD"  # API Key here

def pizo_sensor():
    while True:
        params = urllib.parse.urlencode({'field1': vibration, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(vibration)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
                pizo_sensor()