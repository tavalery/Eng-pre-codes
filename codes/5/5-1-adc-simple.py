import RPi.GPIO as GPIO
import time 


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2bin(x, n):
    # x - int, number to convert
    # n - int, number of symbols
    return [int(elem) for elem in bin(x % (2 ** n))[2:].zfill(n)]
    

def adc():
    for i in range(257):
        GPIO.output(dac, decimal2bin(i, 8))
        time.sleep(0.005)
        if i > 255:
            return i - 1
        if GPIO.input(comp) > 0:
            return i 
    return 0


try:
    while True:
        value = adc()
        # if value != 0:
        print(value, '{:.2f} V'.format(3.3 * value / 256))

except KeyboardInterrupt:
    print('\nClosed by keyboard')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
