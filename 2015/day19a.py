#!/usr/bin/env python

def replacements(string, match, replacement):
	parts = string.split(match)
	for i in xrange(len(parts)-1):
		newstring = match.join(parts[0:i+1])
		newstring += replacement
		newstring += match.join(parts[i+1:])
		yield newstring

def loadsubs(filename):
	with open(filename, 'r') as inputfile:
		table = dict()
		for line in inputfile.read().splitlines():
			if len(line):
				if "=>" in line:
					key, value = line.split(" => ")
					try:
						table[key] += [value]
					except KeyError:
						table[key] = [value]
				else:
					molecule = line
	return table, molecule

def main():
	table, molecule = loadsubs('day19.txt')
	combos = set()
	for tablekey in table:
		for sub in table[tablekey]:
			for newmolecule in replacements(molecule, tablekey, sub):
				combos.add(newmolecule)
	print "{} molecules can be made by applying the substitutions".format(len(combos))
	print combos

if __name__ == '__main__':
	main()
