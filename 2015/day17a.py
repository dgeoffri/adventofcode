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

if __name__ == '__main__':
	main()