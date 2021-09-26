#sourced from here: https://github.com/glenn20/micropython/blob/espnow-g20/docs/library/espnow.rst

#for a sender, though this can be 2-way comm but not sure of configuration changes associated with 2-way


import network
from esp import espnow
w0 = network.WLAN(network.STA_IF) #or can use network.AP_IF
w0.active(True)

e = espnow.ESPNow()
e.init()

peer = b'' #byte string ofd the peer MAC address
e.add_peer(peer)

#example send string, byte or unicode string?
e.send("Starting...")
for i in range(100):
    e.send(peer, str(i)*20, True)
e.send(b'end')


#example receive and setup
#this one is copied directly from source


# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

e = espnow.ESPNow()
e.init()
peer = b'\xaa\xaa\xaa\xaa\xaa\xaa'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        print(host, msg)
        if msg == b'end':
            break
