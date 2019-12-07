#!/usr/bin/env python

def runtape(data):
	ip = 0
	opcode = data[ip]
	while opcode != 99:
		a = data[data[ip + 1]]
		b = data[data[ip + 2]]
		outloc = data[ip + 3]
		if opcode == 1:
			data[outloc] = a + b
		elif opcode == 2:
			data[outloc] = a * b
		ip += 4
		opcode = data[ip]
	return data[0]

def main(argv):
	for noun in xrange(100):
		for verb in xrange(100):
			data = eval("[" + argv[1] + "]")
			data[1] = noun
			data[2] = verb
			if runtape(data) == 19690720:
				print "A noun of %d and a verb of %d produces 19690720 when the tape is run" % (noun, verb)
				break

if __name__ == "__main__":
	import sys
	main(sys.argv)

