import RPi.GPIO as GPIO
import time
import requests

# Nomor pin GPIO yang digunakan untuk mengontrol servo
servo_pin = 12

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Frekuensi PWM (sesuaikan dengan karakteristik servo Anda)
pwm_frequency = 50

# Inisialisasi objek PWM
pwm = GPIO.PWM(servo_pin, pwm_frequency)

def set_servo_angle(angle):
    # Konversi sudut (0-180 derajat) menjadi siklus tugas (duty cycle)
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)

# Fungsi untuk mengambil status switch dari Ubidots
def get_switch_status():
    try:
        url = "https://industrial.api.ubidots.com/api/v1.6/devices/sensors/servo/lv"
        headers = {"X-Auth-Token": "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"}
        response = requests.get(url, headers=headers)
        data = response.json()  # Mengambil data JSON dari respons
        switch_status = int(data[0]['value'])  # Mengambil nilai switch_servo dari data JSON

        return switch_status

    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    try:
        # Mulai PWM
        pwm.start(0)

        while True:
            # Baca status switch dari Ubidots
            switch_status = get_switch_status()

            if switch_status is not None:
                if switch_status == 1:
                    # Jika switch di Ubidots ON, gerakkan servo ke 180 derajat
                    set_servo_angle(180)
                else:
                    # Jika switch di Ubidots OFF, gerakkan servo ke 0 derajat
                    set_servo_angle(0)

            time.sleep(1)

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        set_servo_angle(90)  # Kembalikan servo ke posisi tengah (90 derajat)
        pwm.stop()
        GPIO.cleanup()
