#!/usr/bin/python2

import time
import sys
import requests

EMULATE_HX711 = False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711py.hx711 import HX711
else:
    from hx711py.emulated_hx711 import HX711

GPIO.setmode(GPIO.BCM)

def cleanAndExit():
    if not EMULATE_HX711:
        GPIO.cleanup()

    sys.exit()

def upload_to_ubidots(data_berat):
    UBIDOTS_TOKEN = "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"
    DEVICE_ID = "sensors"
    VARIABLE = "berat"

    # Membuat payload data dalam format JSON
    payload = {
        VARIABLE: data_berat
    }

    # Menyiapkan header dengan token
    headers = {
        "X-Auth-Token": UBIDOTS_TOKEN,
        "Content-Type": "application/json"
    }

    # Mengirim permintaan POST ke Ubidots
    response = requests.post(
        f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}",
        json=payload,
        headers=headers
    )

    print("Data sent to Ubidots:", response.content)
    print("=================")


def main_berat():
    GPIO.setwarnings(False)

    hx = HX711(14, 15)

    hx.set_reading_format("MSB", "MSB")

    hx.set_reference_unit(-2037.46022727273)

    hx.reset()

    hx.tare()

    print("Tare done! Add weight now...")

    try:
        while True:
            val = max(0, int(hx.get_weight(5)))
            data_berat = abs(val)
            print(data_berat, "gr")

            upload_to_ubidots(data_berat)

            hx.power_down()
            hx.power_up()
            time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

if __name__ == "__main__":
    main_berat()
