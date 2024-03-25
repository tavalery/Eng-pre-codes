import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
 
GPIO.setup(leds, GPIO.OUT)
 
def runnung_light(n: int, d=True):
    if d:
        # from left to right
        for i in range(n):
            GPIO.output(leds[i % 8], 1)
            time.sleep(0.2)
            GPIO.output(leds[i % 8], 0)
    else:
        # from right to left
        for i in range(n - 1, 0, -1):
            GPIO.output(leds[i % 8], 1)
            time.sleep(0.2)
            GPIO.output(leds[i % 8], 0)
 
diods_count = 8
 
# first part
runnung_light(diods_count)
 
time.sleep(0.5)
 
# second part
rounds_count = 3
runnung_light(diods_count * rounds_count, 0)
 
GPIO.output(leds, 0)
GPIO.cleanup()