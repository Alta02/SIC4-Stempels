import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def calculate_calibration_factor(berat_tanpa_beban, berat_dengan_beban):
    # Hitung faktor skala
    calibration_factor = (berat_dengan_beban - berat_tanpa_beban) / (berat_dengan_beban - 0)
    return calibration_factor

def main():
    # Konfigurasi pin DT dan SCK
    DT = 6
    SCK = 5

    # Inisialisasi HX711
    hx = HX711(DT, SCK)

    hx.reset()

    print("Letakkan beban pada sensor dan masukkan beratnya.")
    berat_dengan_beban = float(input("Berat dengan beban (gram): "))
    
    print("Tunggu sebentar, lepaskan beban dari sensor.")
    input("Tekan tombol Enter setelah melepaskan beban...")

    # Membaca berat tanpa beban
    berat_tanpa_beban = hx.get_weight_mean(5)

    # Hitung faktor skala
    calibration_factor = calculate_calibration_factor(berat_tanpa_beban, berat_dengan_beban)
    
    print(f"Calibration Factor: {calibration_factor:.2f}")

if __name__ == "__main__":
    main()
