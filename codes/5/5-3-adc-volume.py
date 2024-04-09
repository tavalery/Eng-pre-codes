import RPi.GPIO as GPIO
import time 


leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2bin(x, n):
    # x - int, number to convert
    # n - int, number of symbols
    return [int(elem) for elem in bin(x % (2 ** n))[2:].zfill(n)]


def adc():
    res = 0
    for i in range(7, -1, -1):
        res += 2 ** i 
        GPIO.output(dac, decimal2bin(res, 8))
        time.sleep(0.005)
        if GPIO.input(comp) > 0:
            res -= 2 ** i
    return res 


def comp4leds(num: int, n: int):
    a = [int((n - i) * 255 / 8) for i in range(n)]
    return [1 if num >= elem else 0 for elem in a]#[::-1]


try:
    while True:
        value = adc()
        # if value != 0:
        GPIO.output(leds, comp4leds(value, 8))
        voltage = 3.3 * value / 256
        print(value, '{:.2f} V'.format(voltage))

except KeyboardInterrupt:
    print('\nClosed by keyboard')
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()