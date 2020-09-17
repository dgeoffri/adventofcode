#!/usr/bin/env python

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

loc = [1, 1]

doorcode = ""

def executeline(line):
	for instruction in line:
		if instruction == "U":
			if loc[1] > 0:
				loc[1] -=1
		elif instruction == "D":
			if loc[1] < 2:
				loc[1] +=1
		elif instruction == "L":
			if loc[0] > 0:
				loc[0] -=1
		elif instruction == "R":
			if loc[0] < 2:
				loc[0] +=1
	return keypad[loc[1]][loc[0]]

if __name__ == "__main__":
	with open("day2.txt", "r") as inputfile:
		for line in inputfile:
			doorcode += str(executeline(line.strip()))
		print "The door code is %s" % doorcode

