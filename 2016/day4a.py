#!/usr/bin/env python

import re

def roomIsValid(roomdict):
	roomname = roomdict['roomname'].replace('-','')
	letters = {letter: roomname.count(letter) for letter in set(roomname)}
	checksum = ''.join(sorted(letters, key=lambda item: (letters[item], 255-ord(item)), reverse=True)[:5])
	# print "Their checksum: %s     My checksum: %s" % (roomdict['checksum'], checksum)
	return roomdict['checksum'] == checksum

if __name__ == "__main__":
	with open('day4.txt', 'r') as inputfile:
		inputfile_data = inputfile.readlines()
	rooms = []
	for line in inputfile_data:
		match = re.search(r"(?P<roomname>.*)-(?P<sectorid>\d+)\[(?P<checksum>\w{5})\]", line)
		# print match.groupdict()
		# if roomIsValid(match.groupdict()):
		#	print " - Room is valid!"
		rooms.append(match.groupdict())
	validrooms = filter(roomIsValid, rooms)
	sectorids = [int(room['sectorid']) for room in validrooms]
	# print sectorids
	print "The sum of the sector IDs of the real rooms is %d" % sum(sectorids)
