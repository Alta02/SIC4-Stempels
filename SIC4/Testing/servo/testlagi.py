import RPi.GPIO as GPIO
import time

# Nomor pin GPIO yang digunakan untuk mengontrol servo
servo_pin = 18

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo_pin, GPIO.OUT)

# Frekuensi PWM (sesuaikan dengan karakteristik servo Anda)
pwm_frequency = 50

# Inisialisasi objek PWM
pwm = GPIO.PWM(servo_pin, pwm_frequency)

def set_servo_angle(angle):
    # Konversi sudut (0-180 derajat) menjadi siklus tugas (duty cycle)
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    try:
        # Mulai PWM
        pwm.start(0)

        while True:
            # Gerakkan servo dari 0 derajat hingga 180 derajat
            for angle in range(0, 181, 1):
                set_servo_angle(angle)
                time.sleep(0.01)

            # Kembali gerakkan servo dari 180 derajat ke 0 derajat
            for angle in range(180, -1, -1):
                set_servo_angle(angle)
                time.sleep(0.01)

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        set_servo_angle(90)  # Kembalikan servo ke posisi tengah (90 derajat)
        pwm.stop()
        GPIO.cleanup()
