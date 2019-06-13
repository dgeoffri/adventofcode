#!/usr/bin/env python
# coding: utf-8
import re, sys

correct_aunt_properties = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def load_sues(filename):
	regex=re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$'); 
	try:
		with open(filename, 'r') as inf:
			inputdata=inf.read().splitlines()
	except Exception:
		print "I had some issue reading the input data"
		raise Exception

	sues = dict()

	for line in inputdata:
	    data = regex.match(line).groups()
	    sues[int(data[0])] = { data[1]: int(data[2]), data[3]: int(data[4]), data[5]: int(data[6]) }

	return sues

def main():
	sues = load_sues(sys.argv[1] if len(sys.argv) > 1 else 'day16.txt')
	for auntnumber in sues.keys():
		matches = True
		for prop, value in correct_aunt_properties.items():
			if prop in sues[auntnumber]:
				if sues[auntnumber][prop] != value:
					matches = False
		if matches:
			print "Aunt Sue #%d meets all the criteria!" % (auntnumber)
	
if __name__ == '__main__':
	main()
