#!/usr/bin/env python

PUZZLE_INPUT = 36000000

def howmanypresentsdoesthehouseget(house):
	presents = 0
	for elf in xrange(house, 0, -1):
		if ((house % elf) == 0) and ((elf * 50) <= house):
			presents += (elf*11)
	return presents

def main(): 
	house = 831594 * 2
	numpresents = 0
	while numpresents <= PUZZLE_INPUT:
		print "{} presents delivered to house {}".format(numpresents, house)
		house +=1
		numpresents = howmanypresentsdoesthehouseget(house)
	print house

if __name__ == "__main__":
	main()
