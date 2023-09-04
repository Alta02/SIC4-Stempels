import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup (22,GPIO.OUT)
GPIO.setup (25,GPIO.OUT)
GPIO.setup (5,GPIO.OUT)
GPIO.setup (6,GPIO.OUT)


for i in range(20):
    GPIO.output(22, GPIO.HIGH)
    print("Relay1 lagi nyala")
    time.sleep(0.02)
    GPIO.output(22, GPIO.LOW)
    print("Relay1 lagi mati")
    print("===================")
    time.sleep(0.1)
    
    GPIO.output(25, GPIO.HIGH)
    print("Relay2 lagi nyala")
    time.sleep(0.04)
    GPIO.output(25, GPIO.LOW)
    print("Relay2 lagi mati")
    print("===================")
    time.sleep(0.1)
    
    GPIO.output(5, GPIO.HIGH)
    print("Relay3 lagi nyala")
    time.sleep(0.06)
    GPIO.output(5, GPIO.LOW)
    print("Relay3 lagi mati")
    print("===================")
    time.sleep(0.1)
    
    GPIO.output(6, GPIO.HIGH)
    print("Relay4 lagi nyala")
    time.sleep(0.08)
    GPIO.output(6, GPIO.LOW)
    print("Relay4 lagi mati")
    print("===================")
    time.sleep(0.1)
    
        
GPIO.cleanup()