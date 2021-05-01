from machine import Pin, SoftI2C
from isl29125 import ISL29125
from time import sleep_ms

# I2C init
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
print("I2C Addresses    : "+str(i2c.scan()))
print("I2C Configuration: "+str(i2c)) 

# RGB sensor init to get RGB values with high IR filtering and no use of the interrupt pin
rgbSensor = ISL29125(i2c, configVals=[0x0d, 0x3f, 0x00])

# get status and thresholds
print(rgbSensor.status)
print(rgbSensor.upperThreshold)
print(rgbSensor.lowerThreshold)

while True:
    # get RGB values
    print(rgbSensor.rgbVal)
    sleep_ms(2000)