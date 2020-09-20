#!/usr/bin/env python

keypad = [[False, False, '1', False, False], [False, '2', '3', '4', False], ['5', '6', '7', '8', '9'], [False, 'A', 'B', 'C', False], [False, False, 'D', False, False]]

loc = [2, 0]

doorcode = ""

def executeline(line):
	for instruction in line:
		if instruction == "U":
			if loc[1] > 0:
				if keypad[loc[1]-1][loc[0]]:
					loc[1] -=1
		elif instruction == "D":
			if loc[1] < 4:
				if keypad[loc[1]+1][loc[0]]:
					loc[1] +=1
		elif instruction == "L":
			if loc[0] > 0:
				if keypad[loc[1]][loc[0]-1]:
					loc[0] -=1
		elif instruction == "R":
			if loc[0] < 4:
				if keypad[loc[1]][loc[0]+1]:
					loc[0] +=1
	return keypad[loc[1]][loc[0]]

if __name__ == "__main__":
	with open("day02.txt", "r") as inputfile:
		for line in inputfile:
			doorcode += executeline(line.strip())
		print "The door code is %s" % doorcode

