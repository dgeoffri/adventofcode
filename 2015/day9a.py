#!/usr/bin/env python

import re, itertools

with open('day9.txt', 'r') as inputfile:
	inputdata = inputfile.read().splitlines()
	regex = re.compile(r'(.+) to (.+) = (\d+)')
	cities = set()
	distances=dict()
	for line in inputdata:
		data = regex.match(line).groups()
		cities.add(data[0])
		cities.add(data[1])
		distances[(data[0], data[1])] = int(data[2])
		distances[(data[1], data[0])] = int(data[2])
	results=list()
	for i in itertools.permutations(cities):
		distance = 0
		for j in xrange(len(i)-1):
			distance += distances[(i[j], i[j+1])]
		# print "{} - {} miles".format(', '.join(i), distance)
		results.append([distance, i])
	print "\nThe shortest path is {} miles long".format(sorted(results)[0][0])
