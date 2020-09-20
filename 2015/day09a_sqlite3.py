#!/usr/bin/env python

import re, itertools, sqlite3

with open('day09.txt', 'r') as inputfile:
	inputdata = inputfile.read().splitlines()
	cities = set([i.split(' ')[0] for i in inputdata] + [i.split(' ')[2] for i in inputdata])
	regex = re.compile(r'(.+) to (.+) = (\d+)')
	sqldb = sqlite3.connect(":memory:")
	sqldb.execute("CREATE TABLE distances (city1 VARCHAR, city2 VARCHAR, distance INT);")
	data = [[f(x) for f, x in zip((str, str, int), regex.match(line).groups())] for line in inputdata]
	for i in data:
		sqldb.execute("INSERT INTO distances (city1, city2, distance) VALUES (\"{}\", \"{}\", {});".format(i[0], i[1], i[2]))
		sqldb.execute("INSERT INTO distances (city1, city2, distance) VALUES (\"{}\", \"{}\", {});".format(i[1], i[0], i[2]))
	sqldb.commit()
	results=list()
	for i in itertools.permutations(cities):
		distance = 0
		for j in xrange(len(i)-1):
			distance += sqldb.execute("SELECT distance FROM distances WHERE city1 LIKE '{}' AND city2 LIKE '{}';".format(i[j], i[j+1])).fetchall()[0][0]
		# print "{} - {} miles".format(', '.join(i), distance)
		results.append([distance, i])
	print "\nThe shortest path is {} miles long".format(sorted(results)[0][0])

	
