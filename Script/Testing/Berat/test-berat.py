import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def main():
    # Konfigurasi pin DT dan SCK
    DT = 5
    SCK = 6

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
            
            hx.power_down()
            hx.power_up()
        except (KeyboardInterrupt, SystemExit):
            print("\nMembaca berat selesai.")
            GPIO.cleanup()
            break

if __name__ == "__main__":
    main()
