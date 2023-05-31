from smbus2 import SMBus
from mlx90614 import MLX90614
import time
from time import sleep

import sys
import urlopen
import urllib

from time import sleep
# Enter Your API key here
User1API = '1F2P837WKTCOUF85' 

# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!
buzzer = 21
GPIO.setup(buzzer, GPIO.OUT)
while True:
    
        bus = SMBus(1)
        sensor = MLX90614(bus, address=0x5A)
        print ("Tempreture is :",sensor.get_obj_temp())
        conn = baseURL1 + '&field1=%s' % (sensor.get_obj_temp())
        request = urllib.request.Request(conn)
        responce = urllib.request.urlopen(request)
        responce.close()
        if (sensor.get_obj_temp() > 38.00):
                print("High Tempreture Detected...")
                GPIO.output(buzzer, True)
                time.sleep(1)
                GPIO.output(buzzer, False)
        bus.close()
        sleep(1)
        
                   
        
