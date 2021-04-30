import pycom
import time
from machine import UART

uart = UART(1, 9600)

def setSensor():
    uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3', 'P4'))

def getDistance():
    header_byte = uart.read(1)
    while (header_byte != b'\xff'):
        header_byte = uart.read(1)

    dataH = int(uart.read(1)[0])
    dataL = int(uart.read(1)[0])
    checksum = int(uart.read(1)[0])
    sum = (dataH + dataL - 1)

    if (sum == checksum):
        distance = ((dataH * 256) + dataL)
        return distance
    else:
        return 0
