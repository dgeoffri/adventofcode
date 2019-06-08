#!/usr/bin/env python

PUZZLE_INPUT = 36000000

def howmanypresentsdoesthehouseget(house):
	presents = 0
	for elf in xrange(house, 0, -1):
		if (house % elf) == 0:
			presents += (elf*10)
	return presents

def main(): 
	house = 831594
	while howmanypresentsdoesthehouseget(house) <= PUZZLE_INPUT:
		print "{} presents delivered to house {}".format(howmanypresentsdoesthehouseget(house), house)
		house +=1
	print house
	print PUZZLE_INPUT

if __name__ == "__main__":
	main()
