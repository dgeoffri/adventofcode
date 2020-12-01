#!/usr/bin/env python
import itertools

if __name__ == "__main__":
	inputdata = map(int, file('day01.txt', 'r').read().splitlines())
	for x, y in itertools.combinations(inputdata, 2):
		if x + y == 2020:
			print x * y
