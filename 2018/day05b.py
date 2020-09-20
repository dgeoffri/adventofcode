#!/usr/bin/env python

originalpolymer = list(open('day05.txt', 'r').read().strip())
for letter in "abcdefghijklmnopqrstuvwxyz":
	print "Removing " + letter + "/" + chr(ord(letter) ^ 32)
	polymer = [x for x in originalpolymer if x not in [letter, chr(ord(letter) ^ 32)]]
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
	# print "" + ''.join(polymer)
	print len(polymer)
	if not 'shortest' in locals() or len(polymer) < shortest[1]:
		shortest = (letter, len(polymer))
print "Shortest polymer found by removing " + shortest[0] + "/" + chr(ord(shortest[0])^32) + " for a length of " +str(shortest[1])
