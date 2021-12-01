#!/usr/bin/python3

with open('day01.txt', 'r') as inputfile:
    increased_count = 0
    last_window_sum = 0
    window = []
    for _ in range(3):
        window.append(int(inputfile.readline()))
    last_window_sum = sum(window)
    print("Initial window: {}, sum: {}".format(window, sum(window)))
    for measurement_line in inputfile:
        measurement = int(measurement_line)
        window.append(measurement)
        window.pop(0)
        window_sum = sum(window)
        print("Initial window: {}, sum: {}".format(window, sum(window)))
        if window_sum > last_window_sum:
            increased_count += 1
            print("                  - Increased")
        last_window_sum = window_sum
    print("Window increased {} times".format(increased_count))
