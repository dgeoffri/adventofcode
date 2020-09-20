#!/usr/bin/env python

import array
WIDTH = 16384
HEIGHT = 16384
#WIDTH = 80
#HEIGHT = 80

def printwirearray(wirearray):
	for y in xrange(len(wirearray)):
		print ''.join(wirearray[y])
	print

def findcrossings(wirearray):
	crossings = []
	for y in xrange(len(wirearray)):
		for x in xrange(len(wirearray[y])):
			if wirearray[y][x] == 'X':
				crossings.append((x,y))
	return crossings				
	
def findnearestcrossing(crossings, origin = (WIDTH / 2, HEIGHT / 2)):
	distances = []
	for crossing in crossings:
		distance = (abs(origin[0] - crossing[0])) + abs((origin[1] - crossing[1]))
		distances.append(distance)
	# return sorted(distances)[0]
	distances.sort()
	return distances[0]

def main():
	wirearray = [ array.array('c', '.' * WIDTH) for _ in range(HEIGHT) ]
	origin = (WIDTH / 2, HEIGHT / 2)
	wirearray[origin[0]][origin[1]] = 'o'
	with open('day03.txt', 'r') as f:
		wiredata = f.read().splitlines()
	for wire in wiredata:
		pos = list(origin)
		for movement in wire.split(','):
			direction, distance = movement[0], int(movement[1:])
			if direction == 'R':
				wirechar = '-'
				dirvector = (1, 0)
			elif direction == 'L':
				wirechar = '-'
				dirvector = (-1, 0)
			elif direction == 'U':
				wirechar = '|'
				dirvector = (0, -1)
			elif direction == 'D':
				wirechar = '|'
				dirvector = (0, 1)
			for _ in xrange(distance - 1):
				for axis in (0, 1):
					pos[axis] += dirvector[axis]
				if ((wirechar == '-') and (wirearray[pos[1]][pos[0]] == '|')) or ((wirechar == '|') and (wirearray[pos[1]][pos[0]] == '-')):
					wirearray[pos[1]][pos[0]] = 'X'
				else:
					wirearray[pos[1]][pos[0]] = wirechar
			for axis in (0, 1):
				pos[axis] += dirvector[axis]
			wirearray[pos[1]][pos[0]] = '+'
		wirearray[pos[1]][pos[0]] = wirechar
	printwirearray(wirearray)
	crossings = findcrossings(wirearray)
	print "Crossings found: " + repr(crossings)
	nearestcrossing = findnearestcrossing(crossings, origin = origin)
	print "Closest crossing found has a Manhattan distance of: " + str(nearestcrossing)

if __name__ == "__main__":
	main()

