import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
 
def conver2needed_format(x:int):
    return list(map(int, list((bin(x % 256)[2:].zfill(len(dac))))))
 
data = [255, 127, 64, 32, 5, 0, 256]
res = [conver2needed_format(data[i]) for i in range(len(data))]
 
GPIO.setup(dac, GPIO.OUT)
 
for elem in res:
    GPIO.output(dac, elem)
    time.sleep(15)
    GPIO.output(dac, 0)
 
GPIO.cleanup()