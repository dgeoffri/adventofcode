#!/usr/bin/env python
# coding: utf-8
import re, itertools

regex=re.compile(r'(.+) would (.+) (\d+) happiness units by sitting next to (.+).')
try:
	inputdata=open('day13.txt', 'r').read().splitlines()
except Exception:
	print "I had some issue reading the input data"

names=set()
happiness=dict()

for line in inputdata:
    data = regex.match(line).groups()
    names.add(data[0])
    names.add(data[3])
    if data[1] == 'gain':
        happiness[(data[0], data[3])] = int(data[2])
    elif data[1] == 'lose':
        happiness[(data[0], data[3])] = 0-int(data[2])
del inputdata

# add myself to the list
for name in names:
	happiness[(name, 'me')] = 0
	happiness[('me', name)] = 0
names.add('me')
        
possibilities=set()
for order in itertools.permutations(names):
	total_happiness = 0
	for i in xrange(len(order)):
	    name=order[i]
	    left = order[(i-1) % len(names)]
	    right = order[(i+1) % len(names)]
	    happyleft = happiness[(name, left)]
	    happyright = happiness[(name, right)]
	    print "Sitting next to %s, %s's happiness is affected by %d" % (left, name, happyleft)
	    print "Sitting next to %s, %s's happiness is affected by %d" % (right, name, happyright)
	    print "This affects the total happiness by %d points" % int(happyleft + happyright)
	    total_happiness += happyleft + happyright
	print "The total happiness of this arrangement is", total_happiness, "\n"
	possibilities.add(total_happiness)

print "The best case scenario I saw was a total happiness of", max(possibilities)

