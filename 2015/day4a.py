#!/usr/bin/env python

import sys, hashlib

try:
	inp = sys.argv[1]
except e:
	print "Usage: %s <puzzle input>\n" % sysv.arg[0]

num = 0
while not hashlib.md5(inp + str(num)).hexdigest().startswith('00000'):
	num += 1

print "The answer is:", num
