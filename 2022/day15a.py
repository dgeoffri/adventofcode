#!/usr/bin/env python3

import re
from functools import reduce
from operator import add


class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.sensor = (int(sensor_x), int(sensor_y))
        self.beacon = (int(beacon_x), int(beacon_y))
        self.distance = abs(self.sensor[0] - self.beacon[0]) + abs(self.sensor[1] - self.beacon[1])

    def excluded_points_in_row(self, row):
        row_offset = abs(self.sensor[1] - row)
        if row_offset > self.distance:
            return []
        else:
            min_x = self.sensor[0] - (self.distance - row_offset)
            max_x = self.sensor[0] + (self.distance - row_offset)
            excluded_points = [x for x in range(min_x, max_x + 1)]
            if row == self.beacon[1]:
                excluded_points.remove(self.beacon[0])
            return excluded_points

    def __repr__(self):
        return f"Sensor at x={self.sensor[0]}, y={self.sensor[1]}: closest beacon is at x={self.beacon[0]}, y={self.beacon[1]} - the distance-to-beacon is {self.distance}"


def load_sensors(data):
    inputre = re.compile("Sensor at x=(-?[\d]+), y=(-?[\d]+): closest beacon is at x=(-?[\d]+), y=(-?[\d]+)")
    return [Sensor(*inputre.search(line).groups()) for line in data]


if __name__ == "__main__":
    ROW_TO_CHECK = 2000000

    # ROW_TO_CHECK = 10
    # from io import StringIO
    # puzzle_input = StringIO(
    #     "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3\n")
    puzzle_input = open("day15.txt", "r")
    with puzzle_input as f:
        sensors_and_beacons = f.read().splitlines()
    sensors = load_sensors(sensors_and_beacons)

    excluded_points_in_row = set(reduce(add, (sensor.excluded_points_in_row(ROW_TO_CHECK) for sensor in sensors)))
    print(f"{len(excluded_points_in_row)} points in row {ROW_TO_CHECK} cannot be beacons.")
