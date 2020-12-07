#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day01.txt', 'r') as f:
        inputdata = map(int, f.read().splitlines())
    for x, y, z in itertools.combinations(inputdata, 3):
        if x + y + z == 2020:
            print x * y * z
            break
