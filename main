from machine import I2C
from SI7021 import SI7021
import time

i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)


while True:
    temperature = si7021.temperature()
    humidity = si7021.humidity()
    dew_point = si7021.dew_point()
    serial = si7021.serialnumber
    print(humidity)
    print(temperature)
    time.sleep(1)
