#!/usr/bin/env python

def checkvalid(num):
	numstring = str(num)
	if (not numstring.isdigit()) or (len(numstring) != 6):
		return False
	lastdigit = numstring[0]
	digitrepeated = False
	for digit in numstring[1:]:
		if not digit >= lastdigit:
			return False
		if not digitrepeated and digit == lastdigit:
			digitrepeated = True
		lastdigit = digit
	return digitrepeated

def main(low, high):
	goodpasswords = [ x for x in xrange(low, high) if checkvalid(x) ]
	print "Number of good passwords in range from %d to %d: %d" % (low, high, len(goodpasswords))
		
if __name__ == "__main__":
	import sys
	low = int(sys.argv[1])
	high = int(sys.argv[2])
	main(low, high)
