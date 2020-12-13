#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day10.txt', 'r') as f:
        inputdata = map(int, f.read().splitlines())
    inputdata.sort()
    jolt_differences = {1: 0, 2: 0, 3: 0}
    prev = 0
    for cur in inputdata:
        diff = cur - prev
        if diff not in range(1, 4):
            raise Exception("This won't work")
        else:
            jolt_differences[diff] += 1
        prev = cur
    jolt_differences[3] += 1
    print jolt_differences
    print jolt_differences[1] * jolt_differences[3]