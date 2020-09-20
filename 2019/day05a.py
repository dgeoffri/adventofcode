#!/usr/bin/env python

def main(argv):
	data = eval("[" + argv[1] + "]")
	data[1] = 12
	data[2] = 2
	ip = 0
	opcode = data[ip]
	while opcode != 99:
		a = data[data[ip + 1]]
		b = data[data[ip + 2]]
		outloc = data[ip + 3]
		if opcode == 1:
			data[outloc] = a + b
			ip += 4
		elif opcode == 2:
			data[outloc] = a * b
			ip += 4
		elif opcode == 3:
			data[outloc] = a * b
			ip += 2
		elif opcode == 4:
			data[outloc] = a * b
			ip += 2
		opcode = data[ip]
	print data

if __name__ == "__main__":
	import sys
	main(sys.argv)

