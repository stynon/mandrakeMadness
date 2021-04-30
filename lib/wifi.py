from network import WLAN
import machine
import pycom
import time
import request

def connectSchool():
    wlan = WLAN(mode=WLAN.STA)
    pycom.heartbeat(False)

    wlan.connect(ssid="telenet-4D87F74", auth=(WLAN.WPA2, "x2UcakjTsryz"))

    while not wlan.isconnected():
        time.sleep(1)
        print("WiFi not connected")
        pycom.rgbled(0xFF0000)
    print("WiFi connected succesfully")
    pycom.rgbled(0x00FF00)
    print("test")
    print(wlan.ifconfig())
    print("hond")
    while not wlan.isconnected():
        print("WiFi not connected2.0")
        pycom.rgbled(0xFF0000)
