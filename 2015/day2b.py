#!/usr/bin/env python

total_area = 0
with open('day2.txt', 'r') as infile:
	for box in infile:
		l,w,h=map(int,box.rstrip().split('x'))
		total_area += 2*min(l+w,w+h,h+l)+l*w*h

print "%d feet of ribbon is needed to wrap all the presents" % total_area
