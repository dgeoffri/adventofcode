#!/usr/bin/env python3

class Grid(object):
    def __init__(self):
        self.grid = [[0] * 1024 for _ in range(1024)]
    def __repr__(self):
        return '\n'.join([''.join(map(str,gridline)) for gridline in self.grid])
    def addvent(self, vent):
        ((x1, y1), (x2, y2)) = vent
        print ("Line from ({}, {}) to ({}, {}).".format(x1, y1, x2, y2))
        if (x1 == x2):  # vertical case
            if (y1 > y2):
                (y1, y2) = (y2, y1)
            for y in range(y1, y2 + 1):
                self.grid[y][x1] += 1
        else:
            if (x1 > x2):
                (x1, y1, x2, y2) = (x2, y2, x1, y1)
            if (y1 < y2):
                slope = 1
            elif (y1 > y2):
                slope = -1
            else:
                slope = 0
            y = y1
            for x in range(x1, x2 + 1):
                self.grid[y][x] += 1
                y += slope
    def overlapcount(self):
        return sum([len(list(filter(lambda x: x>1, line))) for line in self.grid])

def parseinput(infile):
    temp = []
    for line in infile:
        src, dst = line.strip().split(' -> ')
        temp.append((tuple(map(int, src.split(','))), tuple(map(int, dst.split(',')))))
    return temp

if __name__ == "__main__":
    with open('day05.txt', 'r') as inputfile:
        vents = parseinput(inputfile)
    grid = Grid()
    for vent in vents:
        grid.addvent(vent)
    print(grid.overlapcount())
