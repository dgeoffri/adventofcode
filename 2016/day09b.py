#!/usr/bin/env python

import re, sys
markersearch = re.compile(r'\(\d+x\d+\)')

def contains_markers(data):
	return True if markersearch.search(data) else False

def decompress(data):
	TEXT = 0
	GETLEN = 1	
	GETCOUNT = 2
	DECOMPRESS = 3

	decompressed_data_length = 0
	repeated_string = ""
	compressed_length = ""
	compressed_count = ""
	state = TEXT

	if not contains_markers(data):
		return len(data)

	data = list(data)
	while len(data):
		nextchar = data.pop(0)
		if state == TEXT:
			if nextchar == "(":
				state = GETLEN
			else:
				decompressed_data_length += 1
		elif state == GETLEN:
			if nextchar == "x":
				state = GETCOUNT
			else:
				compressed_length += nextchar	
		elif state == GETCOUNT:
			if nextchar == ")":
				state = DECOMPRESS
			else:
				compressed_count += nextchar
		elif state == DECOMPRESS:
			repeated_string += nextchar
			for i in xrange(int(compressed_length)-1):
				repeated_string += data.pop(0)
			for i in xrange(int(compressed_count)):
				decompressed_data_length += decompress(repeated_string)
			repeated_string = ""
			compressed_length = ""
			compressed_count = ""
			state = TEXT
	return decompressed_data_length

if __name__ == "__main__":
	with open("day09.txt", "r") as inputfile:
		data = inputfile.read().rstrip()
	decompressed_data_length = decompress(data)
	print "Decompressed data are %d bytes long" % decompressed_data_length
