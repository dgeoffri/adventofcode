#!/usr/bin/env python

from math import sqrt

PUZZLE_INPUT = 36000000

def factors(number):
	factors=list()
	for i in xrange(1, int(sqrt(number))+1):
		if ((number % i) == 0):
			factors.append(i)
			other = number / i
			if other != i:
				factors.append(other)
	return factors

def howmanypresentsdoesthehouseget(house):
	return sum(factors(house))*10

def main(): 
	house = 1
	numpresents = howmanypresentsdoesthehouseget(house)
	while numpresents <= PUZZLE_INPUT:
		# print "{} presents delivered to house {}".format(numpresents, house)
		house +=1
		numpresents = howmanypresentsdoesthehouseget(house)
	print house

if __name__ == "__main__":
	main()
