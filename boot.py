# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import esp32
import network
import machine
from machine import Pin
#esp.osdebug(None)
import webrepl
import neopixel
import time

#LED setup

ledPin = 26
pixels = neopixel.NeoPixel(Pin(ledPin, Pin.OUT), 1)

def pixelWrite(index, rCol, gCol, bCol): #basically I'm lazy and don't want to use the pixels.write each time, now automatic
    pixels[index] = (rCol, gCol, bCol)
    pixels.write()

#set to blue for startup
pixelWrite(0, 0, 0, 125) #blue status: initializing, no network
'''
#network setup
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
print(ap_if.ifconfig()) #print ifconfig

sta_if.active(True)

sta_if.connect('Stammtisch_24', 'cmogbiggs2016')

connected_boolean = sta_if.isconnected()

print(f'Connection status >> {connected_boolean}')

if connected_boolean == True:
    pixelWrite(0, 0, 200, 0)  # green status: inetwork accessed
    print(f'New IP is: >> {sta_if.ifconfig()}')

else:
    pixelWrite(0, 200, 0, 0)  # red status: initializing, no network, initialized
'''
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    pixelWrite(0, 100, 0, 0)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Stammtisch_24', 'cmogbiggs2016')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
pixelWrite(0, 0, 100, 0)


#webrepl.start()
