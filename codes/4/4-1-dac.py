import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2bin(x, n):
    # x - int, number to convert
    # n - int, number of symbols
    return [int(elem) for elem in bin(int(x))[2:].zfill(n)]

def voltage_calculation(s: str, V: float, n: int):
    # V - max possible voltage
    # symbols after ,
    s = s[::-1]
    res = 0
    d = 2
    for i in range(len(s)):
        res += int(s[i]) / d
        d *= 2
    return int((res * V * 10 ** n)) / 10 ** n

try:
    while True:
        val = input('input number from 0 to 255: ')
        if val == 'q':
            break
        elif not val.replace('-', '').replace('.', '').replace(',', '').isdigit():
            print('Wrong type of input, int needed')
        else:
            if str(int(eval(val))) != val:
                print('Number is not int')
            elif int(val) < 0 or int(val) > 255:
                val = int(val)
                print('Number less than zero' * (val < 0) + 'Number greater than 255' * (val > 255))
            else:
                val = int(val)
                res = decimal2bin(val, 8)
                GPIO.output(dac, res)
                res_str = ''.join(map(str, res))
                # print(res_str + ' ' + str(voltage_calculation(res_str, 3.3, 3)) + ' V')
                print(res_str + ' ' + str(val * 3.3 / 255) + ' V')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()