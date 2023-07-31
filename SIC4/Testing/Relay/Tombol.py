import requests
import RPi.GPIO as GPIO
import time

# Pengaturan pin GPIO
GPIO.setmode(GPIO.BCM)

relay_pin1 = 22
GPIO.setup(relay_pin1, GPIO.OUT)
relay_pin2 = 25
GPIO.setup(relay_pin2, GPIO.OUT)
relay_pin3 = 5
GPIO.setup(relay_pin3, GPIO.OUT)
relay_pin4 = 6
GPIO.setup(relay_pin4, GPIO.OUT)

# API token dari Ubidots
api_token = 'BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo'

# URL endpoint untuk mengakses variabel di Ubidots
base_url = 'http://industrial.api.ubidots.com/api/v1.6/devices/'
device_label = 'sensors'
variable_label = 'relay-control'
url = f'{base_url}{device_label}/{variable_label}'

# Fungsi untuk mengaktifkan relay
def turn_relay_on():
    GPIO.output(relay_pin1, GPIO.LOW)
    GPIO.output(relay_pin2, GPIO.LOW)
    GPIO.output(relay_pin3, GPIO.LOW)
    GPIO.output(relay_pin4, GPIO.LOW)

    print("Relay turned ON")

# Fungsi untuk mematikan relay
def turn_relay_off():
    GPIO.output(relay_pin1, GPIO.HIGH)
    GPIO.output(relay_pin2, GPIO.HIGH)
    GPIO.output(relay_pin3, GPIO.HIGH)
    GPIO.output(relay_pin4, GPIO.HIGH)

    print("Relay turned OFF")
    print("==================")

try:
    while True:
        # Mengambil data dari Ubidots
        headers = {'X-Auth-Token': api_token}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            value = data['last_value']['value']
            
            # Memeriksa apakah relay harus diaktifkan atau dimatikan berdasarkan nilai variabel dari Ubidots
            if value == 1:
                turn_relay_on()
            elif value == 0:
                turn_relay_off()
            else:
                print("Nilai variabel tidak valid")
        
        else:
            print("Gagal mendapatkan data dari Ubidots. Status code:", response.status_code)

        # Tunggu sejenak sebelum memperbarui status relay
        time.sleep(0.04)

except KeyboardInterrupt:
    print("Program dihentikan melalui keyboard interrupt")
finally:
    # Memastikan pin GPIO diatur ke nilai awal dan membersihkan GPIO
    GPIO.output(relay_pin, GPIO.LOW)
    GPIO.cleanup()
