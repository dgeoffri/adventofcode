#!/usr/bin/env python

def main(argv):
	with open(argv[1], "r") as f:
		sum = 0
		for module in f.read().splitlines():
			a = int(module)
			b = (a / 3) - 2
			sum += b
		print "Sum is " + str(sum)

if __name__ == "__main__":
	import sys
	main(sys.argv)

