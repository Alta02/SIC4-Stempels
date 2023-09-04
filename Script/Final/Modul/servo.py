import RPi.GPIO as GPIO
import time

def set_servo_angle(pwm, angle):
    # Konversi sudut (0-180 derajat) menjadi siklus tugas (duty cycle)
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)

def main_servo():
    # Inisialisasi GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Nomor pin GPIO untuk masing-masing servo
    servo_pin_7 = 7
    servo_pin_12 = 12
    servo_pin_13 = 13

    # Setup pin GPIO sebagai output untuk masing-masing servo
    GPIO.setup(servo_pin_7, GPIO.OUT)
    GPIO.setup(servo_pin_12, GPIO.OUT)
    GPIO.setup(servo_pin_13, GPIO.OUT)

    # Frekuensi PWM (sesuaikan dengan karakteristik servo Anda)
    pwm_frequency = 50

    # Inisialisasi objek PWM untuk masing-masing servo
    pwm_7 = GPIO.PWM(servo_pin_7, pwm_frequency)
    pwm_12 = GPIO.PWM(servo_pin_12, pwm_frequency)
    pwm_13 = GPIO.PWM(servo_pin_13, pwm_frequency)

    # Mulai PWM untuk masing-masing servo
    pwm_7.start(0)
    pwm_12.start(0)
    pwm_13.start(0)

    count_7 = 0  # Inisialisasi variabel count untuk menghitung putaran servo 7
    count_12 = 0  # Inisialisasi variabel count untuk menghitung putaran servo 12
    count_13 = 0  # Inisialisasi variabel count untuk menghitung putaran servo 13

    try:
        # Gerakkan servo 7 dari 0 derajat hingga 180 derajat
        for angle in range(0, 181, 8):
            set_servo_angle(pwm_7, angle)
            time.sleep(0.01)

        # Kembali gerakkan servo 7 dari 180 derajat ke 0 derajat
        for angle in range(180, -1, -8):
            set_servo_angle(pwm_7, angle)
            time.sleep(0.01)

        count_7 += 1
        print(f"Servo Biru [1] telah berputar selesai sebanyak {count_7} kali.")

        # Gerakkan servo 12 dari 0 derajat hingga 180 derajat setiap 3 putaran servo 7
        if count_7 % 3 == 0:
            for angle in range(0, 181, 8):
                set_servo_angle(pwm_12, angle)
                time.sleep(0.01)

            for angle in range(180, -1, -8):
                set_servo_angle(pwm_12, angle)
                time.sleep(0.01)

            count_12 += 1
            print(f"Servo Biru [2] telah berputar selesai sebanyak {count_12} kali.")

        # Gerakkan servo 13 terus menerus
        for angle in range(0, 181, 8):
            set_servo_angle(pwm_13, angle)
            time.sleep(0.01)

        for angle in range(180, -1, -8):
            set_servo_angle(pwm_13, angle)
            time.sleep(0.01)

        count_13 += 1
        print(f"Servo Hitam [3] telah berputar selesai sebanyak {count_13} kali.")
        print("==========================================")

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        set_servo_angle(pwm_7, 90)
        set_servo_angle(pwm_12, 90)
        set_servo_angle(pwm_13, 90)
        
        pwm_7.stop()
        pwm_12.stop()
        pwm_13.stop()
        
        GPIO.cleanup()

# if __name__ == "__main__":
#     main_servo()
