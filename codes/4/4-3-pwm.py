import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
pwm = GPIO.PWM(2, 10 ** 3)
pwm.start(0)

try:
    while True:
        dc = input('input duty cicle: ')
        if dc == 'q':
            break
        pwm.ChangeDutyCycle(dc)
        print("{:.2f}".format(dc * 3.3 / 100))
finally:
    GPIO.output(2, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()