#!/usr/bin/env python

import sys

txt = sys.argv[1]

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

print len(set(houselist)), "houses are visited at least once"
print '\n'.join(map(repr, houselist))
