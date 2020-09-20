#!/usr/bin/env python

def decompress(data):
	TEXT = 0
	GETLEN = 1	
	GETCOUNT = 2
	DECOMPRESS = 3

	data = list(data)
	decompressed_data = ""
	repeated_string = ""
	compressed_length = ""
	compressed_count = ""
	state = TEXT

	while len(data):
		nextchar = data.pop(0)
		if state == TEXT:
			if nextchar == "(":
				state = GETLEN
			else:
				decompressed_data += nextchar
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
				decompressed_data += repeated_string
			repeated_string = ""
			compressed_length = ""
			compressed_count = ""
			state = TEXT
	return decompressed_data

if __name__ == "__main__":
	with open("day09.txt", "r") as inputfile:
		data = inputfile.read().rstrip()
	decompressed_data = decompress(data)
	print decompressed_data	
	print "Decompressed data are %d bytes long" % len(decompressed_data)
