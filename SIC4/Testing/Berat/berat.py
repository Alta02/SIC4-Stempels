import RPi.GPIO as GPIO
from hx711 import HX711
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

hx = HX711(dout_pin=6, pd_sck_pin=5)

hx.zero()

try:
    # input("Masukan bobot yang diketahui untuk kalibrasi lalu 'enter' : ")
    reading = hx.get_raw_data_mean(readings=10)

    yang_diketahui = input("Masukan bobot dalam gram lalu 'enter ': ")
    hasil = float(yang_diketahui)

    ratio = hasil / reading 
    hx.set_scale_ratio(ratio)

    while True:
        try:
            berat = hx.get_weight_mean()
            print(berat)
        except KeyboardInterrupt:
            print("Keluar dari program.")
            break
        except Exception as e:
            print("Terjadi kesalahan:", e)

except KeyboardInterrupt:
    print("Keluar dari program.")
finally:
    GPIO.cleanup()
