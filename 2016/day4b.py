#!/usr/bin/env python

import re

def decrypt_name(name, id):
	name = name.replace('-', ' ')
	decryptedname = ""
	for character in name:
		if character.isalpha():
			if character.islower():
				decrypted_character = chr(((ord(character) - ord('a') + id) % 26) + ord('a'))
				decryptedname += decrypted_character
			elif character.isupper():
				decrypted_character = chr(((ord(character) - ord('A') + id) % 26) + ord('A'))
				decryptedname += decrypted_character
		else:
			decryptedname += character
	return decryptedname

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

	for room in validrooms:
		sectorid = int(room['sectorid'])
		roomname = room['roomname']
		print "%s - %d" % (decrypt_name(roomname, sectorid), sectorid)
