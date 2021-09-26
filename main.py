import network
import machine
from machine import Pin
import neopixel
import time
from boot import pixelWrite

ledPin = 26

print("Running test colorcycle")
#show that main has initialized

pixels = neopixel.NeoPixel(Pin(ledPin, Pin.OUT), 1)

red = 0
green = 0
blue = 0

pixelWrite(0, red, green, blue)
time.sleep(5)

while True:
    for rr in range(125):
        red = rr
        pixelWrite(0, red, green, blue)
        time.sleep(.01)

    for gg in range(125):
        red = rr - gg
        green = gg
        pixelWrite(0, red, green, blue)
        time.sleep(.01)

    for bb in range(125):
        green = gg - bb
        blue = bb
        pixelWrite(0, red, green, blue)
        time.sleep(.01)
