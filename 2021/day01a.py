#!/usr/bin/python3

with open('day01.txt', 'r') as inputfile:
    increased_count = 0
    last_measurement = int(inputfile.readline())
    for measurement_line in inputfile:
        measurement = int(measurement_line)
        if measurement > last_measurement:
            increased_count += 1
        last_measurement = measurement
    print("Depth increased {} times".format(increased_count))
