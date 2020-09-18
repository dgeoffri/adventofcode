#!/usr/bin/env python

import sys, md5

def printusage(argv):
	print """Usage: %s <Door ID>

The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

This utility will find and display the password (answer to your puzzle) but you must provide the Door ID for me to find the answer!
""" % argv[0]

def showpassword(password):
	printablepassword = [ char if char else '_' for char in password ]
	print "%s" % ' '.join(printablepassword)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		printusage(sys.argv)
		sys.exit(1)

	num=0
	doorname = sys.argv[1]
	print "Finding password for Door ID: %s" % doorname
	password = [False] * 8
	showpassword(password)
	while False in password:
		hex = md5.md5(doorname+str(num)).hexdigest()
		if hex[:5] == '00000':
			position = int(hex[5], 16)
			if (position <= 7) and not password[position]:
				password[position] = hex[6]
				showpassword(password)
		num += 1
	print "The password for Door ID %s is %s" % (doorname, ''.join(password))
