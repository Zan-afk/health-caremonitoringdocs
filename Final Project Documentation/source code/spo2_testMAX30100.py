import time
import max30100

mx30 = max30100.MAX30100()
mx30.enable_spo2()
import sys
import urlopen
import urllib

from time import sleep
# Enter Your API key here
User1API = '1F2P837WKTCOUF85' 

# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API
while 1:
    mx30.read_sensor()

    mx30.ir, mx30.red

    hb = int(mx30.ir / 100)
    spo2 = int(mx30.red / 100)
    
    if mx30.ir != mx30.buffer_ir :
        print("Pulse:",hb);
    if mx30.red != mx30.buffer_red:
        print("SPO2:",spo2);
    conn = baseURL1 + '&field2=%s&field3=%s' % (hb,spo2)
    request = urllib.request.Request(conn)
    responce = urllib.request.urlopen(request)
    responce.close()
    time.sleep(2)
