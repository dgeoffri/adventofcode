#!/usr/bin/env python3

import operator
from functools import reduce

def floodfill(heightmap, coords):
    x, y = coords
    try:
        if heightmap[y][x] == 9 or x < 0 or y < 0:
            return 0
        heightmap[y][x] = 9
        return sum([floodfill(heightmap, (x + 1, y)),
        floodfill(heightmap, (x - 1, y)), 
        floodfill(heightmap, (x, y - 1)),
        floodfill(heightmap, (x, y + 1))], 1)
    except IndexError:
        return 0
        
def findlowpoints(heightmap):
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            curheight = heightmap[y][x]
            if y > 0 and heightmap[y - 1][x] <= curheight:
                continue
            if x > 0 and heightmap[y][x - 1] <= curheight:
                continue
            if x <(len(heightmap[0]) - 1) and heightmap[y][x + 1] <= curheight:
                continue
            if y < (len(heightmap) - 1) and heightmap[y + 1][x] <= curheight:
                continue
            yield (x, y)
            
if __name__ == "__main__":
    with open("day09.txt", "r") as inputfile:
        inputlist = inputfile.read().splitlines()
        heightmap = [[int(x) for x in list(line)] for line in inputlist]
    lowpoints = tuple(findlowpoints(heightmap))
    print("The low points are at {}".format(lowpoints))
    basins = [ floodfill(heightmap, lowpoint) for lowpoint in lowpoints ]
    largest_basins = sorted(basins)[-3:]
    print("The three largest basins are {}".format(tuple(largest_basins)))
    print("The product of their areas is: {}".format(reduce(operator.mul, largest_basins)))
