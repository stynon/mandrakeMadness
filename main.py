from machine import I2C
from machine import Pin
from SI7021 import SI7021
import time
import ultrasonic
import adafruit

#connect to Sigfox
import sigfox

relay = Pin('P2', mode=Pin.OUT)
i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)

while True:
    temperature = si7021.temperature()
    humidity = si7021.humidity()
    dew_point = si7021.dew_point()
    serial = si7021.serialnumber

    ultrasonic.setSensor()
    distance = ultrasonic.getDistance()

    print(str(round(humidity,2)) + " %")
    print(str(round(temperature,2)) + " °C")
    print(str(round(distance,2)) + " mm")

    if humidity <= 70:
        relay.value(1)
        sigfox.sigfoxConnect(humidity)
        print(humidity)
    else:
        relay.value(0)
        sigfox.sigfoxConnect(humidity)
    time.sleep(1)
