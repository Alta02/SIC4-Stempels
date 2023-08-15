import RPi.GPIO as GPIO
import time

# Atur mode GPIO ke BCM
GPIO.setmode(GPIO.BCM)

# Tentukan nomor pin GPIO yang digunakan
sensor_pin = 23

# Set pin sebagai input
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sensor_pin):
            print("Air terdeteksi")
        else:
            print("Tidak ada air")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
