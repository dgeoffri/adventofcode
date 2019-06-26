#!/usr/bin/env python

import sys, hashlib

try:
	inp = sys.argv[1]
except Exception as e:
	print "Usage: %s <puzzle input>\n" % sys.argv[0]
	sys.exit(1)

num = 0
while not hashlib.md5(inp + str(num)).hexdigest().startswith('00000'):
	num += 1

print "The answer is:", num
