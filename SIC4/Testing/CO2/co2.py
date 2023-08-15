import time
import board
import busio
import adafruit_ccs811

i2c_bus = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c_bus)

while not ccs811.data_ready:
    pass

while True:
    if ccs811.data_ready:
        print("eCO2: {} ppm, TVOC: {} ppb".format(ccs811.eco2, ccs811.tvoc))
    time.sleep(1)
