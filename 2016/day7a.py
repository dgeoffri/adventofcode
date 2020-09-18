#!/usr/bin/env python

import re

def has_abba(group):
	abba = False
	if len(group) < 4:
		return False
	for index in range(len(group) - 3):
		if not abba:
			quad = group[index:index+4]
			if (quad[0] != quad[1]) and (quad[0] == quad[3]) and (quad[1] == quad[2]):
				abba = True
	return abba
		
	
def getgroups(address):
	hypernets = re.findall(r"\[(\w+)\]", address)
	addressgroups = [group for group in re.findall(r"[^\[\]]+", address) if group not in hypernets]

	return {'hypernets': hypernets, 'addressgroups': addressgroups}

def supports_TLS(address):
	groupdict = getgroups(address)
	for group in groupdict['hypernets']:
		if has_abba(group):
			return False
	abba = False
	for group in groupdict['addressgroups']:
		if not abba:
			if has_abba(group):
				abba = True
	return abba

if __name__ == "__main__":
	with open("day7.txt", "r") as inputfile:
		inputfile_data = inputfile.readlines()
	addresses_with_TLS = filter(supports_TLS, inputfile_data)
	print "%d addresses support TLS" % len(addresses_with_TLS)
	
