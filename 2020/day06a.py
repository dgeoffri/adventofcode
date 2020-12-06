#!/usr/bin/env python

if __name__ == "__main__":
    with open('day06.txt', 'r') as f:
        inputdata = [x.split() for x in f.read().split('\n\n')]
    sum = 0
    for group in inputdata:
        sum += len(reduce(lambda x, y: x | y, map(set, list(group))))
    print sum
