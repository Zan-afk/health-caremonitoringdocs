

import Adafruit_ADS1x15
import serial
import time
import requests
import random
import json
import urllib
from gtts import gTTS
# Enter Your API key here
User1API = 'FFKD5BXO78M7P2NK'
# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API

rate = [0]*10
amp = 100
GAIN = 2/3  
curState = 0
stateChanged = 0

ser = serial.Serial ("/dev/ttyS0", 9600)

import random
import json
import urllib
# Enter Your API key here
User1API = 'FFKD5BXO78M7P2NK'
# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API
import pygame

def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 4096  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

def send_to_prcessing1(data1):   # for tempreture Sensor
        ser.write(str(data1).encode())


def flex():
        adc = Adafruit_ADS1x15.ADS1115()
        while True:
                Signal = adc.read_adc(1, gain=GAIN)   
                send_to_prcessing1(Signal)
                message = str(Signal / 3.5)
                print("Flex:" + str(message))
                conn = baseURL1 + '&field8=%s' % (message)
                request = urllib.request.Request(conn)
                responce = urllib.request.urlopen(request)
                responce.close()
                if message < '0':
                    message = 0.0
                    
                if str(message) >= '4800':
                       tts = gTTS('I want water for drinking')
                       tts.save('1.mp3')
                       initMixer()
                       file = '/home/pi/22E9556-Health_Monitoring/1.mp3'
                       pmusic(file)
                       print("I want water for drinking")
                       print("Their is bend occured in the bridge")   
                        
                       
                send_to_prcessing1(message)
                time.sleep(0.5)
               

                    
flex()

