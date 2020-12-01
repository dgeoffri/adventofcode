#!/usr/bin/env python
import itertools

if __name__ == "__main__":
	inputdata = map(int, file('day01.txt', 'r').read().splitlines())
	for x, y, z in itertools.combinations(inputdata, 3):
		if x + y + z == 2020:
			print x * y * z
