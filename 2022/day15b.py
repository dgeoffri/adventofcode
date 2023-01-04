#!/usr/bin/env python3

import re
from functools import reduce
from operator import add


class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.sensor = (int(sensor_x), int(sensor_y))
        self.beacon = (int(beacon_x), int(beacon_y))
        self.distance = abs(self.sensor[0] - self.beacon[0]) + abs(self.sensor[1] - self.beacon[1])

    def excluded_points_in_row(self, row, rowmin=None, rowmax=None):
        row_offset = abs(self.sensor[1] - row)
        if row_offset > self.distance:
            return []
        else:
            min_x = self.sensor[0] - (self.distance - row_offset)
            max_x = self.sensor[0] + (self.distance - row_offset)
            # optional clamp
            if rowmin is not None:
                min_x = max(min_x, rowmin)
            if rowmax is not None:
                max_x = min(max_x, rowmax)
            excluded_points = [x for x in range(min_x, max_x + 1)]
            if row == self.beacon[1] and self.beacon[0] in excluded_points:
                excluded_points.remove(self.beacon[0])
            return excluded_points

    def point_in_range(self, coord):
        return (abs(self.sensor[0] - coord[0]) + abs(self.sensor[1] - coord[1])) <= self.distance

    def trace_perimeter(self):
        yield (self.sensor[0], self.sensor[1] - self.distance - 1)
        for row in range(self.sensor[1] - self.distance, self.sensor[1] + self.distance):
            row_offset = abs(self.sensor[1] - row)
            left = self.sensor[0] - (self.distance - row_offset) - 1
            right = self.sensor[0] + (self.distance - row_offset) + 1
            yield (left, row)
            yield (right, row)
        yield (self.sensor[0], self.sensor[1] + self.distance + 1)

    def __repr__(self):
        return f"Sensor at x={self.sensor[0]}, y={self.sensor[1]}: closest beacon is at x={self.beacon[0]}, y={self.beacon[1]} - the distance-to-beacon is {self.distance}"


def load_sensors(data):
    inputre = re.compile("Sensor at x=(-?[\d]+), y=(-?[\d]+): closest beacon is at x=(-?[\d]+), y=(-?[\d]+)")
    return [Sensor(*inputre.search(line).groups()) for line in data]


def find_hole(sensors, search_range=(0, 4000000)):
    for perimeter_sensor in sensors:
        for point in perimeter_sensor.trace_perimeter():
            if (search_range[0] <= point[0] <= search_range[1]) and (search_range[0] <= point[1] <= search_range[1]):
                for check_sensor in sensors:
                    if perimeter_sensor is check_sensor:
                        continue
                    if check_sensor.point_in_range(point):
                        break
                else:
                    return point


if __name__ == "__main__":
    SEARCH_RANGE = (0, 4000000)

    # SEARCH_RANGE = (0, 20)
    # from io import StringIO
    # puzzle_input = StringIO(
    #     "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3\n")
    puzzle_input = open("day15.txt", "r")
    with puzzle_input as f:
        sensors_and_beacons = f.read().splitlines()
    sensors = load_sensors(sensors_and_beacons)
    hole = find_hole(sensors, SEARCH_RANGE)
    print(hole)
    print(f"Tuning frequency is {hole[0] * 4000000 + hole[1]}")
