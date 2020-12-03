#!/usr/bin/env python

if __name__ == "__main__":
    with open('day03.txt', 'r') as f:
        inputdata = f.read().splitlines()
    x = 0
    trees = 0
    for y in xrange(len(inputdata)):
        if inputdata[y][x % len(inputdata[y])] == "#":
            trees += 1
        x += 3
    print "Encountered %d trees" % trees
