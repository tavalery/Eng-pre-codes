import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20 ,26, 16, 19, 25, 23, 24]
 
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
 
while True:
    GPIO.output(leds, [GPIO.input(aux[i]) for i in range(len(aux))])
    time.sleep(0.1)
 
GPIO.output(leds, 0)
 
GPIO.cleanup()