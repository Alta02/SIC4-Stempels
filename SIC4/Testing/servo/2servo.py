import RPi.GPIO as GPIO
import time

# GPIO pins used to control the servos
servo_pins = [12, 13, 18]

# Initialization GPIO
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins as outputs for the servos
for servo_pin in servo_pins:
    GPIO.setup(servo_pin, GPIO.OUT)

# PWM frequency (adjust according to your servo's characteristics)
pwm_frequency = 50

# Create PWM objects for each servo
pwms = [GPIO.PWM(servo_pin, pwm_frequency) for servo_pin in servo_pins]

def set_servo_angle(pwm, angle):
    # Convert angle (0-180 degrees) to duty cycle
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    try:
        # Start PWM for each servo
        for pwm in pwms:
            pwm.start(0)

        counts = [0] * len(servo_pins)  # Initialize count variables for each servo

        while True:
            for i, pwm in enumerate(pwms):
                # Move each servo from 0 degrees to 360 degrees clockwise
                for angle in range(0, 361, 1):
                    set_servo_angle(pwm, angle)
                    time.sleep(0.01)

                # Return the servo to the initial position (0 degrees)
                set_servo_angle(pwm, 0)
                time.sleep(1)

                # Increment the corresponding count variable for each servo
                counts[i] += 1
                print(f"Servo {i + 1} telah berputar selama {counts[i]} kali.")

    except KeyboardInterrupt:
        # Stop PWM and clean up GPIO when the program is terminated with Ctrl+C
        for pwm in pwms:
            set_servo_angle(pwm, 90)  # Return each servo to the middle position (90 degrees)
            pwm.stop()

        GPIO.cleanup()
