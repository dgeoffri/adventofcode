#!/usr/bin/env python

import sys, md5

def printusage(argv):
	print """Usage: %s <Door ID>

The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

This utility will find and display the password (answer to your puzzle) but you must provide the Door ID for me to find the answer!
""" % argv[0]

if __name__ == "__main__":
	if len(sys.argv) != 2:
		printusage(sys.argv)
		sys.exit(1)

	num=0
	doorname = sys.argv[1]
	print "Finding password for Door ID: %s" % doorname
	password = ""
	for i in range(8):
		while True:
			hex = md5.md5(doorname+str(num)).hexdigest()
			if hex[:5] == '00000':
				password += hex[5]
				num += 1
				break
			num += 1
	print "The password for Door ID %s is %s" % (doorname, password)
