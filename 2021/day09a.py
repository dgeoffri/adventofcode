#!/usr/bin/env python3

def findlowpoints(heightmap):
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            curheight = int(heightmap[y][x])
            if y>0 and int(heightmap[y-1][x]) <= curheight:
                continue
            if x>0 and int(heightmap[y][x-1]) <= curheight:
                continue
            if x<(len(heightmap[0])-1) and int(heightmap[y][x+1]) <= curheight:
                continue
            if y<(len(heightmap)-1) and int(heightmap[y+1][x]) <= curheight:
                continue
            yield curheight
            
if __name__ == "__main__":
    with open("day09.txt", "r") as inputfile:
        heightmap = inputfile.read().splitlines()
    print("The low points are {}".format(tuple(findlowpoints(heightmap))))
    print("The risk level is {}".format(sum(map(lambda x:x+1, findlowpoints(heightmap)))))
