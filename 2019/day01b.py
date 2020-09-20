#!/usr/bin/env python

def calcfuelformass(mass):
	return max(0, (mass / 3) - 2)

def main(argv):
	with open(argv[1], "r") as f:
		sum = 0
		for module in f.read().splitlines():
			a = int(module)
			fuel = calcfuelformass(a)
			newfuel = calcfuelformass(fuel)
			while (newfuel > 0):
				fuel += newfuel
				newfuel = calcfuelformass(newfuel)
			sum += fuel
		print "Sum is " + str(sum)

if __name__ == "__main__":
	import sys
	main(sys.argv)

