#!/usr/bin/env python
# coding: utf-8
import re

SECONDS = 2503

regex=re.compile(r'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
try:
	inputdata=open('day14.txt', 'r').read().splitlines()
except Exception:
	print "I had some issue reading the input data"

capabilities=dict()

for line in inputdata:
    data = regex.match(line).groups()
    capabilities[data[0]] = tuple(map(int, data[1:4]))
del inputdata

states=dict()
distances=dict()
points=dict()

for deer in capabilities:
	states[deer] = list(capabilities[deer][1:])
	distances[deer] = 0
	points[deer] = 0

for _ in xrange(SECONDS):
	for deer in distances:
		if states[deer][0] > 0:
			distances[deer] += capabilities[deer][0]
			states[deer][0] -= 1
		elif states[deer][1] > 1:
			states[deer][1] -=1
		else:
			states[deer] = list(capabilities[deer][1:])
	furthest_distance = max(distance for deer, distance in distances.items())
	for deer in distances:
		if distances[deer] == furthest_distance:
			points[deer] += 1

print "{} seconds have elapsed!".format(SECONDS)

for deer, score in sorted(points.items(), key=lambda x:x[1]):
	print "{} has {} points.".format(deer, score)
