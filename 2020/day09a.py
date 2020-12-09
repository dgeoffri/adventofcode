#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day09.txt', 'r') as f:
        inputdata = map(int, f.read().splitlines())
    failed = False
    while not failed:
        if len(filter(lambda (x, y): x + y == inputdata[25], itertools.combinations(inputdata[:25], 2))) < 1:
            failing_number = inputdata[25]
            failed = True
        else:
            inputdata.pop(0)
    print "Number {} fails the check!".format(failing_number)