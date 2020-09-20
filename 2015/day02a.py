#!/usr/bin/env python

import sys

total_area = 0
with open(sys.argv[1] if len(sys.argv) > 1 else 'day02.txt', 'r') as infile:
	for box in infile:
		l,w,h=map(int,box.rstrip().split('x'))
		total_area += 2*l*w+2*w*h+2*h*l+min(l*w,w*h,h*l)

print "%d square feet of wrapping paper is needed to wrap all the presents" % total_area
