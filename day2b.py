#!/usr/bin/env python

infile=open('day2.txt')
boxids=infile.read().splitlines()

while boxids:
	boxtocompare = boxids.pop(0)
	for box2 in boxids:
		box3=bytearray(box2)
		differingletters=0
		for index in xrange(len(boxtocompare)):
			if boxtocompare[index] != box2[index]:
				differingletters+=1
				box3[index]='.'
		print "%s and %s differ by %d letters (%s)" % (boxtocompare, box2, differingletters, str(box3))

			
