import requests
import RPi.GPIO as GPIO
import time

# Pengaturan pin GPIO
GPIO.setmode(GPIO.BCM)

relay_pins = [22, 25, 5, 6]
for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)

# API token dari Ubidots
api_token = 'BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo'

# URL endpoint untuk mengakses variabel di Ubidots
base_url = 'http://industrial.api.ubidots.com/api/v1.6/devices/'
device_label = 'sensors'
variable_labels = ['relay-control', 'relay-control2', 'relay-control3', 'relay-control4']

urls = [f'{base_url}{device_label}/{label}' for label in variable_labels]

# Fungsi untuk mengaktifkan relay
def turn_relay_on(relay_pin):
    GPIO.output(relay_pin, GPIO.LOW)
    print(f"Relay {relay_pin} turned ON")

# Fungsi untuk mematikan relay
def turn_relay_off(relay_pin):
    GPIO.output(relay_pin, GPIO.HIGH)
    print(f"Relay {relay_pin} turned OFF")
    print("==================")

try:
    while True:
        for i in range(len(urls)):
            # Mengambil data dari Ubidots untuk setiap variabel
            headers = {'X-Auth-Token': api_token}
            response = requests.get(urls[i], headers=headers)

            if response.status_code == 200:
                data = response.json()
                value = data['last_value']['value']

                # Memeriksa apakah relay harus diaktifkan atau dimatikan berdasarkan nilai variabel dari Ubidots
                if value == 1:
                    turn_relay_on(relay_pins[i])
                elif value == 0:
                    turn_relay_off(relay_pins[i])
                else:
                    print(f"Nilai variabel {variable_labels[i]} tidak valid")

            else:
                print(f"Gagal mendapatkan data dari Ubidots untuk variabel {variable_labels[i]}. Status code:", response.status_code)

        # Tunggu sejenak sebelum memperbarui status relay
        time.sleep(0.04)

except KeyboardInterrupt:
    print("Program dihentikan melalui keyboard interrupt")
finally:
    # Memastikan pin GPIO diatur ke nilai awal dan membersihkan GPIO
    for pin in relay_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
