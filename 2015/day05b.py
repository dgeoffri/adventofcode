#!/usr/bin/env python

nicestrings = []

with open ('day05.txt', 'r') as inputfile:
	for line in inputfile:
		word = line.rstrip()
		alllocations = []
		for i in range(len(word)-1):
			pair = word[i:i+2]
			locations = []
			for j in range(len(word)-1):
				if word[j:j+2] == pair:
					locations.append(j)
					if len(locations) > 1:
						alllocations.append(locations)
		for locations in alllocations:
			startposition=locations[0]
			for position in locations[1:]:
				if position > startposition+1:
					for i in range(len(word)-2):
						if word[i] == word[i+2]:
							nicestrings.append(word)
print len(set(nicestrings))
