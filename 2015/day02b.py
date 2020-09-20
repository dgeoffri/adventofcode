#!/usr/bin/env python

import sys

total_length = 0
with open(sys.argv[1] if len(sys.argv) > 1 else 'day02.txt', 'r') as infile:
	for box in infile:
		l,w,h=map(int,box.rstrip().split('x'))
		total_length += 2*min(l+w,w+h,h+l)+l*w*h

print "%d feet of ribbon is needed to wrap all the presents" % total_length