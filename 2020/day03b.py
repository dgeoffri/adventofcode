#!/usr/bin/env python

if __name__ == "__main__":
    with open('day03.txt', 'r') as f:
        inputdata = f.read().splitlines()
    treeslist = []
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    for xslope, yslope in slopes:
        x = 0
        trees = 0
        for y in xrange(0, len(inputdata), yslope):
            if inputdata[y][x % len(inputdata[y])] == "#":
                trees += 1
            x += xslope
        treeslist.append(trees)
    print "Encountered %d trees" % reduce(lambda i, j: i*j, treeslist)
