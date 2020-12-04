#!/usr/bin/env python

def find_distance(coords):
	return reduce(lambda x, y: x + y, map(abs, list(coords)))

def main():
	with open('day03.txt', 'r') as f:
		wiredata = f.read().splitlines()
	wirelocations = []
	for wirenumber, wiremovements in enumerate(wiredata):
		pos = [0, 0]
		wirelocations.append([])
		for movement in wiremovements.split(','):
			direction, distance = movement[0], int(movement[1:])
			if direction == 'R':
				dirvector = (1, 0)
			elif direction == 'L':
				dirvector = (-1, 0)
			elif direction == 'U':
				dirvector = (0, -1)
			elif direction == 'D':
				dirvector = (0, 1)
			for _ in xrange(distance):
				for axis in (0, 1):
					pos[axis] += dirvector[axis]
				wirelocations[wirenumber].append(tuple(pos))
	wiresets = map(set, wirelocations)
	crossings = reduce(lambda x, y: x & y, wiresets)
	print "Closest intersection is {} units away.".format(min(map(find_distance, list(crossings))))

if __name__ == "__main__":
	main()
