#!/usr/bin/env python

nicestrings = []

with open ('day5.txt', 'r') as inputfile:
	for line in inputfile:
		word = line.rstrip()
		vowelcount = sum([word.count(x) for x in 'aeiou'])
		if vowelcount >= 3:
			lastcharacter=''
			for character in word:
				if character == lastcharacter:
					for badcombo in ['ab', 'cd', 'pq', 'xy']:
						if badcombo in word:
							break
					else:
						nicestrings.append(word)
				lastcharacter = character

print len(set(nicestrings))
