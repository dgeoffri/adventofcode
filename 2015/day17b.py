#!/usr/bin/env python

import itertools

def read_jars(filename):
	jars = []
	with open('day17.txt', 'r') as f:
		for line in map(str.rstrip, f):
			jars.append(int(line))
	return jars

def main():
	jars = read_jars('day17.txt')
	combos = [filter(lambda x: sum(x)==150, itertools.combinations(jars,i)) for i in xrange(len(jars))]
	print "{} combinations are possible".format(sum(map(len,combos)))
	for i in xrange(len(combos)):
		if len(combos[i]) > 0:
			minimum_jars = i
			break
	print "The minimum number of jars needed to hold 150 litres is {}".format(minimum_jars)
	print "There are {} combinations possible with {} jars".format(len(combos[minimum_jars]), minimum_jars)

if __name__ == '__main__':
	main()