#!/usr/bin/env python

import re

def getgroups(address):
	hypernets = re.findall(r"\[(\w+)\]", address)
	addressgroups = [group for group in re.findall(r"[^\[\]]+", address) if group not in hypernets]
	return {'hypernets': hypernets, 'addressgroups': addressgroups}

def has_bab(group):
	bablist = set()
	if len(group) < 3:
		return bablist
	for index in range(len(group) - 2):
		triad = group[index:index+3]
		if (triad[0] != triad[1]) and (triad[0] == triad[2]):
			bablist.add(triad)
	return bablist

def has_aba_for_bab(grouplist, bablist):
	for group in grouplist:
		for bab in bablist:
			if (bab[0] == bab[1]) or (bab[0] != bab[2]):
				print "Error: bab is not a bab!"
				return False
			aba = bab[1] + bab[0] + bab[1]
			if aba in group:
				return True	
	return False

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

def supports_SSL(address):
	groupdict = getgroups(address)
	bablist = reduce(lambda x, y: x | y, [ has_bab(group) for group in groupdict['hypernets'] ])
	return has_aba_for_bab(groupdict['addressgroups'], bablist)

if __name__ == "__main__":
	with open("day07.txt", "r") as inputfile:
		inputfile_data = inputfile.readlines()
	addresses_with_TLS = filter(supports_TLS, inputfile_data)
	print "%d addresses support TLS" % len(addresses_with_TLS)
	addresses_with_SSL = filter(supports_SSL, inputfile_data)
	print "%d addresses support SSL" % len(addresses_with_SSL)
	
