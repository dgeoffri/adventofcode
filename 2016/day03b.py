#!/usr/bin/env python

def isATriangle(sides):
	a, b, c = sides
	return (a + b > c) and (b + c > a) and (a + c > b)

if __name__ == "__main__":
	line = dict()
	EOF = False
	potentialtriangles = []
	with open ("day3.txt", "r") as trianglefile:
		trianglefile_lines = trianglefile.readlines()
	while len(trianglefile_lines) >= 3:
		for i in range(3):
			readline = trianglefile_lines.pop().rstrip()
			line[i] = tuple(map(int, readline.split()))
		# print line
		potentialtriangles += [tuple(line[i][j] for i in range(3)) for j in range(3)]
	# print potentialtriangles
	print "There are %d valid triangles in the file" % len(filter(isATriangle, potentialtriangles))

