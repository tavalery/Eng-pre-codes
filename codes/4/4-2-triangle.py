import RPi.GPIO as GPIO
import time 

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2bin(x, n):
    # x - int, number to convert
    # n - int, number of symbols
    return [int(elem) for elem in bin(int(x))[2:].zfill(n)]

try:
    while True:
        T = input('input period (T): ')
        if T == 'q':
            break
        elif not T.replace('-', '').replace('.', '').replace(',', '').isdigit():
            print('Wrong type of input, number needed')
        else:
            t = eval(T) / 2 ** 9
            for s1 in range(2 ** 8):
                GPIO.output(dac, decimal2bin(s1, 8))
                time.sleep(t)
            for s1 in range(2 ** 8 - 1, -1):
                GPIO.output(dac, decimal2bin(s1, 8))
                time.sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()