# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def getting_data():
    with open('settings.txt') as file:
        settings = [float(elem) for elem in file.read().split('\n')]
    
    with open('data.txt') as file:
        data = np.array([int(elem) for elem in file.read().rstrip().split('\n')])
    
    data_volts = data / 256 * 3.3
    data_time = np.array([ind / settings[0] for ind in range(len(data))])
    
    return (data_time, data_volts)


def get_borders(data: np.array, coef: int):
    Delta = np.mean(data[1:] - data[:-1]) * coef
    min_ = min(data) - Delta
    max_ = max(data) + Delta
    return [min_, max_]


def graph(X: np.array, Y: np.array, d: int):
    #print('Graph creating process')
    
    plt.figure(figsize=(8, 6), dpi=100)
    
    borders = get_borders(X, 2) + get_borders(Y, 4)
    plt.axis(borders)
    
    plt.grid(True, which='major', color='grey', linestyle="-")
    plt.minorticks_on()
    plt.grid(True, which='minor', color='grey', linestyle=":")

    plt.plot(X, Y, color='b', linewidth=1, label = 'V(t)')
    # !!! options from the tests (lms), but all do not work 
    #T, N = np.mean(X[1:] - X[:-1]), len(X) // 3
    #marker_indexes = np.linspace(0, T * (N - 1), N)
    #marker_indexes = np.linspace(0, len(X) - 1, N)
    #marker_indexes = np.arange(0, T * N, T)
    #X_markers = [X[int(ind)] for ind in marker_indexes]
    #Y_markers = [Y[int(ind)] for ind in marker_indexes]
    #plt.scatter(X_markers, Y_markers, marker='s', c='blue', s=10)    
    plt.scatter(X[0:len(X):d], Y[0:len(Y):d], marker='s', c='blue', s=10)  # variant for weak  
    
    plt.title('Процесс заряда и разряда конденсатора в RC-цепи', loc='center')
    plt.xlabel('Time, sec')
    plt.ylabel('Voltage, V')
    
    x1, y1 = (borders[0] * 7 + borders[1]) / 8, (borders[2] * 3 + borders[3]) / 4 # increasing part
    x2, y2 = (borders[0] * 3 + borders[1] * 5) / 8, y1                            # decreasing part
    peak_time_index = Y.argmax()
    peak_time = X[peak_time_index]
    charging_time, discharging_time = round(peak_time - min(X), 2), round(max(X) - peak_time, 2)
    plt.text(x1, y1, 'Время заряда = {} сек'.format(charging_time))
    plt.text(x2, y2, 'Время разряда = {} сек'.format(discharging_time))
    
    plt.legend(shadow=False, loc='upper right', fontsize=12)
    plt.show()

    plt.savefig('graph.png')
    plt.savefig('graph.svg')


def main():
    data_time, data_volts = getting_data()
    graph(data_time, data_volts, 10)


main()
