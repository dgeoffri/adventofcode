#!/usr/bin/env python

polymer = list(open('day05.txt', 'r').read().strip())
length = len(polymer)-1
index = 0
while index < length:
	if (ord(polymer[index]) == ord(polymer[index+1])^32):
		del polymer[index]
		del polymer[index]
		length-=2
		index-=1
		if index < 0: index = 0
	else:
		index += 1
print "" + ''.join(polymer)
print len(polymer)
