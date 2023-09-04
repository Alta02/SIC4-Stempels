import RPi.GPIO as GPIO
import time

# Konfigurasi pin
PIN_OUT = 17

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_OUT, GPIO.IN)

counter = 0
prev_state = 0
total_steps = 1000  # Jumlah langkah (pulsa) per putaran lengkap
reset_pattern = [1, 0, 1]  # Pola putaran untuk reset (contoh)

reset_buffer = []

def check_reset():
    global reset_buffer
    if reset_buffer == reset_pattern:
        global counter
        counter = 0
        print("Persentase diatur ulang menjadi 0%")
    reset_buffer = []

def rotary_callback(channel):
    global prev_state, counter, reset_buffer
    state = GPIO.input(PIN_OUT)
    reset_buffer.append(state)
    if len(reset_buffer) > len(reset_pattern):
        reset_buffer.pop(0)
    check_reset()

    if state != prev_state:
        if state == 1:
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            counter = total_steps - 1
        elif counter >= total_steps:
            counter = 0
        percentage = (counter / total_steps) * 100
        print(f"Telah berputar: {percentage:.2f}%")
    prev_state = state

# Tambahkan event handler untuk interrupt saat perubahan pada pin OUT
GPIO.add_event_detect(PIN_OUT, GPIO.BOTH, callback=rotary_callback)

try:
    while True:
        time.sleep(0.1)  # Jeda agar skrip tetap berjalan

except KeyboardInterrupt:
    GPIO.cleanup()

