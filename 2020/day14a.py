#!/usr/bin/env python

if __name__ == "__main__":
    with open('day14.txt', 'r') as f:
        inputdata = map(lambda x: x.split(" = "), f.read().splitlines())
    memory = {}
    for instruction in inputdata:
        if instruction[0] == "mask":
            or_mask = int(instruction[1].replace("X", "0"), 2)
            and_mask = int(instruction[1].replace("X", "1"), 2)
            print "mask:     {}".format(instruction[1])
            print "or_mask:  {}".format(instruction[1].replace("X", "0"))
            print "and_mask: {}".format(instruction[1].replace("X", "1"))

        elif instruction[0].startswith("mem["):
            addr = int(instruction[0][4:-1])
            val = int(instruction[1])
            memory[addr] = (val & and_mask) | or_mask
    print sum(memory.values())
