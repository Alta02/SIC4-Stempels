import time
import sys

EMULATE_HX711 = False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx = HX711(18, 17)

hx.set_reading_format("MSB", "MSB")

hx.set_reference_unit(-522)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()

def main():
    try:
        # 1. Inisiasi berat awal
        previous_weight = hx.get_weight()
        print("Current weight on the scale in grams is:", previous_weight)

        while True:
            # 2. Cek berat tiap sekian menit
            current_weight = hx.get_weight()
            delta_weight = previous_weight - current_weight 

            print("Current Weight : ", current_weight)
            print("Previous Weight : ", previous_weight)
            print("Delta Weight : ", delta_weight)

            berat_botol = 225
            if current_weight > berat_botol:
                # Lainnya...
                pass

            # sleep tiap 30 menit
            time.sleep(30)

    except (KeyboardInterrupt, SystemExit):
        print("Membaca beban selesai.")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
