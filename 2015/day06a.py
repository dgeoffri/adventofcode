#!/usr/bin/env python

import re, array, textwrap
from ast import literal_eval

lightarray = [array.array('B', (0 for _ in xrange(1000))) for _ in xrange(1000)]

with open('day6.txt', 'r') as inputfile:
	regex = re.compile(r'(.*) (\d+,\d+) through (\d+,\d+)')
	for line in inputfile:
		match = regex.match(line)
		groups = [i(j) for i, j in zip((str, literal_eval, literal_eval), match.groups())]
		# print "'" + groups[0] + "'"
		if groups[0] == 'turn on':
			for y in xrange(groups[1][1], groups[2][1] + 1):
				for x in xrange(groups[1][0], groups[2][0] + 1):
					lightarray[y][x] = 1
		elif groups[0] == 'turn off':
			for y in xrange(groups[1][1], groups[2][1] + 1):
				for x in xrange(groups[1][0], groups[2][0] + 1):
					lightarray[y][x] = 0
		elif groups[0] == 'toggle':
			for y in xrange(groups[1][1], groups[2][1] + 1):
				for x in xrange(groups[1][0], groups[2][0] + 1):
					lightarray[y][x] ^= 1

	lightcount = 0
	for y in xrange(1000):
		lightcount += lightarray[y].count(1)
	print lightcount, 'lights are lit after following the instructions'

	
with open('day6a.pgm', 'wb') as f:
	f.write('P2\n1000 1000\n1\n')
	for y in xrange(1000):
		f.write('\n'.join(textwrap.wrap(' '.join(map(str, lightarray[y])), width=70))+'\n')
