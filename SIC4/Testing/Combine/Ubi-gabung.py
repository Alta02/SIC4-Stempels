import RPi.GPIO as GPIO
import time
import requests
import json

GPIO.setmode(GPIO.BCM)

# Ultrasonic sensor GPIO pins
GPIO_Trigger = 23
GPIO_echo = 24

# Touch sensor GPIO pin
TOUCH_SENSOR_PIN = 17

GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setup(GPIO_echo, GPIO.IN)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN)

# Ubidots configuration
UBIDOTS_TOKEN = "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"
DEVICE_LABEL_ULTRA = "sensors"
VARIABLE_LABEL_ULTRA = "ultra"
DEVICE_LABEL_TOUCH = "sensors"
VARIABLE_LABEL_TOUCH = "sentuh"

def distance():
    GPIO.output(GPIO_Trigger, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_Trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_echo) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_echo) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def send_data_to_ubidots(device_label, variable_label, value):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/values"
    headers = {"Content-Type": "application/json", "X-Auth-Token": UBIDOTS_TOKEN}
    payload = {"value": value}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Data sent to Ubidots successfully!")
    else:
        print("Failed to send data to Ubidots")

try:
    while True:
        dist = distance()
        print("Measured Distance = %.2f cm" % dist)
        send_data_to_ubidots(DEVICE_LABEL_ULTRA, VARIABLE_LABEL_ULTRA, dist)
        print("=========================================")

        touch_detected = GPIO.input(TOUCH_SENSOR_PIN)
        print("Touch Detected:", touch_detected)
        send_data_to_ubidots(DEVICE_LABEL_TOUCH, VARIABLE_LABEL_TOUCH, touch_detected)
        print("=========================================")


        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
