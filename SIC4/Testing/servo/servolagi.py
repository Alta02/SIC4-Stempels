import RPi.GPIO as GPIO
import time

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

if __name__ == "__main__":
    try:
        # Mulai PWM
        pwm.start(0)

        count = 0  # Inisialisasi variabel count untuk menghitung berapa kali servo telah berputar

        while True:
            # Gerakkan servo dari 0 derajat hingga 360 derajat searah jarum jam
            for angle in range(0, 361, 1):
                set_servo_angle(angle)
                time.sleep(0.01)

            # Kembalikan servo ke posisi awal (0 derajat)
            set_servo_angle(0)
            time.sleep(1)

            # Tambahkan 1 ke variabel count setiap kali servo bergerak searah jarum jam
            count += 1
            print(f"Servo telah berputar selama {count} kali.")

    except KeyboardInterrupt:
        # Hentikan PWM dan reset GPIO saat program berhenti dengan Ctrl+C
        set_servo_angle(90)  # Kembalikan servo ke posisi tengah (90 derajat)
        pwm.stop()
        GPIO.cleanup()
