#!/usr/bin/python

from ast import literal_eval

with open('day8.txt', 'r') as inputfile:
	b=inputfile.read().splitlines()
	c=map(literal_eval, b)
	print "The difference between the number of characters of code for string literals and the number of characters in memory for the values of the strings in total for the entire file is:", sum(map(len, b))-sum(map(len, c))
