import RPi.GPIO as GPIO
import time

# Nomor pin GPIO yang digunakan untuk mengontrol servo
servo_pin = 4

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Frekuensi PWM (sesuaikan dengan karakteristik servo Anda)
pwm_frequency = 50

# Inisialisasi objek PWM
pwm = GPIO.PWM(servo_pin, pwm_frequency)

def set_servo_angle(angle):
    duty_cycle = (angle / 18.0) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)  # Waktu tunggu untuk menyesuaikan sudut servo (sesuaikan jika perlu)

if __name__ == "__main__":
    try:
        # Mulai PWM
        pwm.start(0)

        while True:
            # Gerakan servo dari 0 derajat hingga 180 derajat dengan selang waktu 1 detik
            for angle in range(0, 181, 10):
                set_servo_angle(angle)

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        pwm.stop()
        GPIO.cleanup()
