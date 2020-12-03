#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day01.txt', 'r') as f:
        inputdata = map(int, f.read().splitlines())
    for x, y in itertools.combinations(inputdata, 2):
            if x + y == 2020:
                print x * y
