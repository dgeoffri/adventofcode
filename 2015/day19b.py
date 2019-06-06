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
	table, targetmolecule = loadsubs('day19.txt')

	table = { "e": ["H", "O"], "H": ["HO", "OH"], "O": ["HH"] }
	targetmolecule = 'HOHOHO'

	combos = set('e')
	iterations = 0
	newcombos = set()
	while targetmolecule not in combos:
		for tablekey in table:
			for sub in table[tablekey]:
				for mol in combos:
					for newmolecule in replacements(mol, tablekey, sub):
						newcombos.add(newmolecule)
		combos = set(newcombos)
		iterations += 1
		print combos
		print "{} iterations, combos is {} elements long now".format(iterations, len(combos))
	print "Found the molecule after {} iterations.".format(iterations)

if __name__ == '__main__':
	main()
