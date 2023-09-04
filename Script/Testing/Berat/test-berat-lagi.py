#!/usr/bin/python2

import time
import sys

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("RPi.GPIO module not available. Running in emulation mode.")
    EMULATE_HX711 = True
else:
    EMULATE_HX711 = False

referenceUnit = 1

if not EMULATE_HX711:
    from hx711 import HX711

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(-2037.46022727273)
hx.set_offset(0.93)
hx.reset()
hx.tare()

print("Tare done! Add weight now...")

while True:
    try:
        val = hx.get_weight(5)
        data_berat = abs(val)
        print(data_berat)

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
