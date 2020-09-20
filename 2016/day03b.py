#!/usr/bin/env python

def isATriangle(sides):
	a, b, c = sides
	return (a + b > c) and (b + c > a) and (a + c > b)

if __name__ == "__main__":
	line = dict()
	EOF = False
	potentialtriangles = []
	with open("day03.txt", "r") as inputfile:
		triangles = inputfile.readlines()
	while len(triangles) >= 3:
		for i in range(3):
			readline = triangles.pop().rstrip()
			line[i] = tuple(map(int, readline.split()))
		# print line
		potentialtriangles += [tuple(line[i][j] for i in range(3)) for j in range(3)]
	# print potentialtriangles
	print "There are %d valid triangles in the file" % len(filter(isATriangle, potentialtriangles))

