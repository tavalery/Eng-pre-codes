import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

# experiment settings
leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2bin(x, n):
    # x - int, number to convert
    # n - int, number of symbols
    return [int(elem) for elem in bin(x % (2 ** n))[2:].zfill(n)]

 
# getting data from troyka
def adc():
    res = 0
    for i in range(7, -1, -1):
        res += 2 ** i 
        GPIO.output(dac, decimal2bin(res, 8))
        time.sleep(0.005)
        if GPIO.input(comp) > 0:
            res -= 2 ** i
    return res


def graph(X: list, Y: list):
    print('Graph creating process')
    pyplot.plot(X, Y)
    pyplot.xlabel('time, sec')
    pyplot.ylabel('Voltage, V')
    pyplot.show()

 
try:
    voltage = 0
    result_data = []
    time_start = time.time()
    count = 0
    
    # first parf of experiment
    print("Start of capacitor's charging")
    while voltage < 206: #256 * 0.9: # < 200 for less time
        voltage = adc()
        result_data.append(voltage)
        print(voltage)
        time.sleep(0)
        count += 1
        GPIO.output(leds, decimal2bin(voltage, 8))
 
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
    
    # second part of experiment
    print("Start of capacitor's discharging")
    while voltage > 176: #169: #256 * 0.02: # without zeros
        voltage = adc()
        result_data.append(voltage)
        print(voltage)
        time.sleep(0)
        count += 1
        GPIO.output(leds, decimal2bin(voltage, 8))
 
    time_experiment = time.time() - time_start
    
    # fix data in file
    print('Addind data to file')
    with open('7/data.txt', 'w') as f:
        for item in result_data:
            f.write(str(item) + '\n')
    with open('7/settings.txt', 'w') as f:
        f.write(str(1 / time_experiment / count) + '\n')
        f.write('0.01289')
    
    # print('time_experiment:', round(time_experiment, 3), 'sec')
    # print('1 priod time:', round(time_experiment/count, 3), 'sec')
    print('общая продолжительность эксперимента:', round(time_experiment, 3), 'sec')
    print('период одного измерения:', round(time_experiment / count, 3), 'sec')
    print('средняя частота дискретизации:', round(10 ** 3 * 1 / time_experiment / count, 3), 'mHz')
    print('шаг квантования АЦП:', 0.01289)

    # making graph
    X = [i * time_experiment / count for i in range(len(result_data))]
    Y = [i / 256 * 3.3 for i in result_data]
    graph(X, Y)

    
finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()