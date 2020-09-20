#!/usr/bin/python

def encode(string):
	return "\"" + ''.join(map(lambda y: "\\"+y if (y=="\\" or y=="\"") else y, string)) + "\""

with open('day08.txt', 'r') as inputfile:
	b=inputfile.read().splitlines()
	c=map(encode, b)
	print "The difference between the total number of characters to represent the newly encoded strings and the number of characters of code in each original string literal is:", sum(map(len, c))-sum(map(len, b))
