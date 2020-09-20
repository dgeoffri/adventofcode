#!/usr/bin/env python

def checkvalid(num):
	numstring = str(num)
	if (not numstring.isdigit()) or (len(numstring) != 6):
		return False
	lastdigit = numstring[0]
	digitsrepeated = set()
	for digit in numstring[1:]:
		if not digit >= lastdigit:
			return False
		if digit == lastdigit:
			digitsrepeated.add(digit)
		lastdigit = digit
	for x in digitsrepeated:
		if numstring.count(x) == 2:
			return True
	return False

def main(low, high):
	goodpasswords = [ x for x in xrange(low, high) if checkvalid(x) ]
	print "Number of good passwords in range from %d to %d: %d" % (low, high, len(goodpasswords))
		
if __name__ == "__main__":
	import sys
	low = int(sys.argv[1])
	high = int(sys.argv[2])
	main(low, high)
