import RPi.GPIO as GPIO
import time

# Nomor pin GPIO yang digunakan untuk mengontrol servo 1 (360 derajat)
servo_1_pin = 13 

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_1_pin, GPIO.OUT)

# Frekuensi PWM (sesuaikan dengan karakteristik servo Anda)
pwm_frequency = 50

# Inisialisasi objek PWM untuk servo 1
pwm_1 = GPIO.PWM(servo_1_pin, pwm_frequency)

def set_servo_speed(pwm_obj, speed):
    # speed harus berada di antara -100 hingga 100
    duty_cycle = (speed + 100) / 18.0
    pwm_obj.ChangeDutyCycle(duty_cycle)

if _name_ == "_main_":
    try:
        # Mulai PWM untuk servo 1
        pwm_1.start(0)

        # Atur kecepatan servo 1 untuk berputar searah jarum jam
        # set_servo_speed(pwm_1, 50)  # Kecepatan setengah maksimum (searah jarum jam)

        while True:
            pwm_1.ChangeDutyCycle(5)
            time.sleep(1)
            pwm_1.ChangeDutyCycle(10)
            time.sleep(1)            
            pwm_1.ChangeDutyCycle(15)
            time.sleep(1)
            pwm_1.ChangeDutyCycle(10)
            time.sleep(1)
            pwm_1.ChangeDutyCycle(5)
            time.sleep(1)

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        set_servo_speed(pwm_1, 0)  # Hentikan pergerakan servo 1
        pwm_1.stop()
        GPIO.cleanup()