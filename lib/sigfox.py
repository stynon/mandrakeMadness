from network import Sigfox
import socket
import math

def sigfoxConnect(humidity):
    # init Sigfox for RCZ1 (Europe)
    sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

    # create a Sigfox socket
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

    # make the socket blocking
    s.setblocking(True)

    # configure it as uplink only
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

    print("connected")

    # send some bytes
    s.send(bytes([humidity]))
    print("send done")
