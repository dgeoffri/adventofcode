#!/usr/bin/env python

import sys

txt = open(sys.argv[1] if len(sys.argv) > 1 else "day3.txt").read().rstrip()

curloc = { 'Santa': [0,0], 'Robo-Santa': [0,0] }
cursanta = 'Santa'

houselist = []

houselist.append(tuple(curloc['Santa']))
houselist.append(tuple(curloc['Robo-Santa']))

for move in txt:
	if move == '^':
		curloc[cursanta][0]+=1
	elif move == 'v':
		curloc[cursanta][0]-=1
	elif move == '>':
		curloc[cursanta][1]+=1
	elif move == '<':
		curloc[cursanta][1]-=1
	houselist.append(tuple(curloc[cursanta]))
	cursanta = 'Robo-Santa' if cursanta=='Santa' else 'Santa'

print '\n'.join(map(repr, houselist))
print len(set(houselist)), "houses are visited at least once"
