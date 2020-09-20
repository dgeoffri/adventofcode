#!/usr/bin/env python

def isATriangle(sides):
	a, b, c = sides
	return (a + b > c) and (b + c > a) and (a + c > b)

if __name__ == "__main__":
	with open ("day3.txt", "r") as trianglefile:
		potentialtriangles = [tuple(map(int, line.rstrip().split())) for line in trianglefile]
		print "There are %d valid triangles in the file" % len(filter(isATriangle, potentialtriangles))
