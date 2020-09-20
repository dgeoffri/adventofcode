#!/usr/bin/env python

def isATriangle(sides):
	a, b, c = sides
	return (a + b > c) and (b + c > a) and (a + c > b)

if __name__ == "__main__":
	with open("day03.txt", "r") as inputfile:
		potentialtriangles = [tuple(map(int, line.rstrip().split())) for line in inputfile]
		print "There are %d valid triangles in the file" % len(filter(isATriangle, potentialtriangles))
