import RPi.GPIO as GPIO
import time
import requests

# Nomor pin GPIO yang digunakan untuk mengontrol servo
servo_pin = 13

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo_pin, GPIO.OUT)

# Frekuensi PWM (sesuaikan dengan karakteristik servo Anda)
pwm_frequency = 50

# Inisialisasi objek PWM
pwm = GPIO.PWM(servo_pin, pwm_frequency)

def set_servo_angle(angle):
    # Batasi sudut di antara 0 dan 180 derajat
    angle = max(0, min(180, angle))
    # Konversi sudut (0-180 derajat) menjadi siklus tugas (duty cycle)
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)

# Ubidots API settings
DEVICE_ID = "sensors"
API_TOKEN = "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"
SERVO_CONTROL_VARIABLE = "servo"

# Function to turn servo on
def turn_servo_on():
    set_servo_angle(180)  # Set servo angle to turn it on

# Function to turn servo off
def turn_servo_off():
    set_servo_angle(0)  # Set servo angle to turn it off

if __name__ == "__main__":
    try:
        # Mulai PWM
        pwm.start(0)

        count = 0  # Inisialisasi variabel count untuk menghitung putaran

        while True:
            # Retrieve servo control data from Ubidots
            response = requests.get(f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}/{SERVO_CONTROL_VARIABLE}/lv?token={API_TOKEN}")
            servo_control = float(response.content)  # Convert response content to a float

            # Control the servo based on Ubidots data
            if servo_control == 1.0:  # Check if the servo control value is 1.0 (on)
                turn_servo_on()
            elif servo_control == 0.0:  # Check if the servo control value is 0.0 (off)
                turn_servo_off()

            # Gerakkan servo dari 0 derajat hingga 180 derajat dengan increment 5 derajat
            for angle in range(0, 181, 5):
                set_servo_angle(angle)
                time.sleep(0.01)  # Kurangi nilai waktu sleep untuk pergerakan lebih cepat

            # Kembali gerakkan servo dari 180 derajat ke 0 derajat dengan decrement 5 derajat
            for angle in range(180, -1, -5):
                set_servo_angle(angle)
                time.sleep(0.01)  # Kurangi nilai waktu sleep untuk pergerakan lebih cepat

            # Tambahkan 1 ke variabel count setiap kali servo bergerak selesai satu putaran
            count += 1
            print(f"Servo telah berputar selesai sebanyak {count} kali.")
            print("==========================================")

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        set_servo_angle(90)  # Kembalikan servo ke posisi tengah (90 derajat)
        pwm.stop()
        GPIO.cleanup()
