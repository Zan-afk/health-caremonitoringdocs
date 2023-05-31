#!/usr/bin/python

import time
import requests
import json
import Adafruit_ADS1x15
import smtplib
import requests
import json
from email.message import EmailMessage

location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
print(location_obj)
lat = location_obj['latitude']
lon = location_obj['longitude']
city = "%s, %s, \n\r %s, %s" % (lat,lon,location_obj['city'], location_obj['region_code'])


import requests
import random
import json
import urllib
import urlopen
# Enter Your API key here
User1API = '1F2P837WKTCOUF85'
# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
VALMAX = 15000
GAIN = 1
adcValue = 0;
offsetVoltage = 100;
msg ="Patient Falled....Here I attached mylocation:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude)
def sms_send():
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"fvaKUPuNimZCWE8MOpB9YjLGs4nyeg6lzRqS71JXH5QFw3cktDIm3puGNrOFLP2Bq0AzjDfsWtVCTe6x",
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":"9607181257"
    }
    rs=requests.get(url,params=params)


def mapp( x, in_min, in_max, out_min, out_max) :
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def sensor_position ():
	pos = 0
	x = adc.read_adc(0, gain=GAIN)
	y = adc.read_adc(1, gain=GAIN)
	z = adc.read_adc(2, gain=GAIN)

	Xval = mapp (x,0,VALMAX,0,255)
	Yval = mapp (y,0,VALMAX,0,255)
	Zval = mapp (z,0,VALMAX,0,255)
	print ("X:"+str (Xval))
	print ("Y:"+str (Yval))
	print ("Z:"+str (Zval))
	conn = baseURL1 + '&field4=%s&field5=%s&field6=%s' % (Xval,Yval,Zval)
	request = urllib.request.Request(conn)
	responce = urllib.request.urlopen(request)
	responce.close()
	time.sleep(2)
	if (Xval > 429 or Xval < 410) :
		pos = 1	
		return pos	
	if (Yval > 442 or Yval < 420) :
		pos = 1
		return pos
	else:
		pos = 0
		return pos
	
	

# Main loop.
while True:
	pos = sensor_position()
	
	if pos == 1 :
		print("Patient Falled")
		
	else :
		print("Normal Condition")	
		
	time.sleep(1)


