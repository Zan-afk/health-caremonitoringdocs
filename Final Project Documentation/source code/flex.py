

import Adafruit_ADS1x15
import serial
import time
import requests
import random
import json

# Enter Your API key here
User1API = '1F2P837WKTCOUF85'
# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API

rate = [0]*10
amp = 100
GAIN = 2/3  
curState = 0
stateChanged = 0
ser = serial.Serial ("/dev/ttyAMA0", 9600)

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


def flex1():
        adc = Adafruit_ADS1x15.ADS1015()
        while True:
                Signal = adc.read_adc(0, gain=GAIN)   
                send_to_prcessing1(Signal)
                message = str(Signal / 3.5)
                print("Flex:" + str(message))
                conn = baseURL1 + '&field7=%s' % (message)
                request = urllib.request.Request(conn)
                responce = urllib.request.urlopen(request)
                responce.close()
                if message < '0':
                    message = 0.0
                    
                if str(message) >= '1':
                        from gtts import gTTS
                        tts = gTTS('I want water for drinking')
                        tts.save('1.mp3')
                        initMixer()
                        file = '/home/pi/22E9556-Health_Monitoring/1.mp3'
                        pmusic(file)
                        print("I want water for drinking")   
                        
                       
                send_to_prcessing1(message)
                time.sleep(0.5)
               
def flex2():
        adc = Adafruit_ADS1x15.ADS1015()
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
                    
                if str(message) >= '1':
                        from gtts import gTTS
                        tts = gTTS('"I want to go washroom"')
                        tts.save('2.mp3')
                        initMixer()
                        file = '/home/pi/22E9556-Health_Monitoring/2.mp3'
                        pmusic(file)
                        print("I want to go washroom")   
                       
                       
                send_to_prcessing1(message)
                time.sleep(0.5)

                    
while True:
    flex1()
    flex2()
