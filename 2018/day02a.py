#!/usr/bin/env python

infile=open('day2.txt')
bw2,bw3=set(), set()
for boxid in infile:
	letters={}
	for l in boxid:
		if l in letters:
			letters[l]+=1
		else:
			letters[l]=1
	for letter in letters:
		if letters[letter] == 2:
			bw2.add(boxid.strip())
		if letters[letter] == 3:
			bw3.add(boxid.strip())

print "Box IDs with 2 identical letters:"
for boxid in bw2:
	print boxid

print "Box IDs with 3 identical letters:"
for boxid in bw3:
	print boxid

print "%d box IDs with 2 identical letters * %d box IDs with 3 identical letters = checksum %d" % (len(bw2), len(bw3), len(bw2)*len(bw3))
