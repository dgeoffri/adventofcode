#!/usr/bin/env python

import sys

txt = open(sys.argv[1] if len(sys.argv)>1 else "day3.txt", "r").read().rstrip()

curloc = [0,0]

houselist = []

houselist.append(tuple(curloc))
for move in txt:
	if move == '^':
		curloc[0]+=1
	elif move == 'v':
		curloc[0]-=1
	elif move == '>':
		curloc[1]+=1
	elif move == '<':
		curloc[1]-=1
	houselist.append(tuple(curloc))

print '\n'.join(map(repr, houselist))
print len(set(houselist)), "houses are visited at least once"
