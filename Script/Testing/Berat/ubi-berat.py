import RPi.GPIO as GPIO
from hx711 import HX711
import requests

# Inisialisasi pin GPIO
GPIO.setmode(GPIO.BCM)

# Ubidots configuration
UBIDOTS_TOKEN = "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"
DEVICE_LABEL = "sensors"
BERAT_VARIABLE_LABEL = "berat"

def send_berat_to_ubidots(berat):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{BERAT_VARIABLE_LABEL}/values"
    headers = {"Content-Type": "application/json", "X-Auth-Token": UBIDOTS_TOKEN}
    payload = {"value": berat}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Data berat sent to Ubidots successfully!")
    else:
        print("Failed to send data berat to Ubidots")

def main():
    try:
        # Konfigurasi pin DT dan SCK
        DT = 6
        SCK = 5

        # Inisialisasi HX711
        hx = HX711(DT, SCK)

        # Ganti nilai faktor skala sesuai dengan hasil perhitungan Anda
        calibration_factor = 2433.15

        hx.reset()

        print("Bacaan berat dimulai...")

        while True:
            try:
                # Ambil 5 bacaan berat dan hitung rata-ratanya
                weight = hx.get_weight_mean(5)

                # Konversi pembacaan ke berat dalam gram
                adjusted_weight = max(weight / calibration_factor - 15.0, 0.0)
                
                print(f"Berat: {adjusted_weight:.2f} g")
                
                # Kirim data berat ke Ubidots
                send_berat_to_ubidots(adjusted_weight)

                hx.power_down()
                hx.power_up()

            except (KeyboardInterrupt, SystemExit):
                print("\nMembaca berat selesai.")
                break

    finally:
        # Bersihkan GPIO saat program berhenti
        GPIO.cleanup()

if __name__ == "__main__":
    main()
