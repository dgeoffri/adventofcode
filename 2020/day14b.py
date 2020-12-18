#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day14.txt', 'r') as f:
        inputdata = map(lambda x: x.split(" = "), f.read().splitlines())
    memory = {}
    mask = format(0, '036b')
    for instruction in inputdata:
        if instruction[0] == "mask":
            mask = instruction[1]
        elif instruction[0].startswith("mem["):
            addr = int(instruction[0][4:-1])
            binaddr = format(addr, "036b")
            value = int(instruction[1])
            addrlist = [['0', '1'] if mask[x] == 'X' else [str(int(binaddr[x]) | int(mask[x]))] for x in range(len(mask))]
            addresses = map(lambda x: int(x, 2), map(''.join, itertools.product(*addrlist)))
            for address in addresses:
                memory[address] = value
    print sum(memory.values())