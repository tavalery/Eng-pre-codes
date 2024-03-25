import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
 

def controlled(n: int, time: int)
    for i in range(n):
        value = GPIO.input(24)
        GPIO.output(25, value)
        time.sleep(time)


def uncontrolled()
    while True:
        GPIO.output(25, GPIO.input(24))
