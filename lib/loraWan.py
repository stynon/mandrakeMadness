from network import LoRa
import socket
import time
import ubinascii
import ustruct

def loraConnect():
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    app_eui = ubinascii.unhexlify('70B3D57ED003E4C4')
    app_key = ubinascii.unhexlify('2F77C58DD6AB59F1A603976A6792A598')
    dev_eui = ubinascii.unhexlify('70B3D549943157B4')
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)
    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')
    print('Joined')

def send(data):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(False)
    packet = ustruct.pack('f',data)
    s.send(packet)
    s.setblocking(False)
