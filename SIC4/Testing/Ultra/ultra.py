import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_Trigger = 17
GPIO_echo = 27

# Set up GPIO pins as output and input
GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setup(GPIO_echo, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_Trigger, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_Trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# Detecting an object
def object_detection(distance):
    # Jika jarak dibawah 200 cm maka status adalah bahaya
    status = "aman"
    if distance < 280:
        status = "bahaya"
    if distance <= 150:
        status = "sangat bahaya"
    return status
    
if __name__ == "__main__":
    while True:
        try:
            # Distance detection
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            status = object_detection(dist)
            print("Status adalah:", status)
            # Gap time for sound 
            time.sleep(1)
        except KeyboardInterrupt:
            # Clean up GPIO on keyboard interrupt
            GPIO.cleanup()
            break
