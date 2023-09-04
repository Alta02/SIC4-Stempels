#!/usr/bin/python2

import time
import sys

EMULATE_HX711 = False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    if not EMULATE_HX711:
        GPIO.cleanup()

    sys.exit()
    
GPIO.setwarnings(False)

hx = HX711(14, 15)

hx.set_reading_format("MSB", "MSB")

hx.set_reference_unit(-2037.46022727273)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

while True:
    try:
        val = max(0, int(hx.get_weight(5)))
        data_berat = abs(val)
        print(data_berat, "gr")
        print("=================")

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
