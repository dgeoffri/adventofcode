#!/usr/bin/env python

if __name__ == "__main__":
	with open("day6.txt", "r") as inputfile:
		inputfile_contents = map(str.rstrip, inputfile.readlines())
	plaintext = ""
	for x in range(len(inputfile_contents[0])):
		letterlist = [ inputfile_contents[i][x] for i in range(len(inputfile_contents)) ]
		letterdict = { letter: letterlist.count(letter) for letter in set(letterlist) }
		plaintext += sorted(letterdict, key = letterdict.__getitem__)[0]
	print plaintext
