#!/usr/bin/env python

class computer(object):
    def __init__(self, instructions):
        self.instructions = []
        for line in instructions:
            instruction = line.split()
            self.instructions.append([instruction[0], int(instruction[1])])
    def do_nop(self, operand):
        self.IP += 1
    def do_acc(self, operand):
        self.acc += operand
        self.IP += 1
    def do_jmp(self, operand):
        self.IP += operand
    def run(self):
        self.IP = 0
        self.acc = 0
        self.visited = []
        while True:
            # print "IP: %d, acc: %d, instr: %s, operand: %d" % (self.IP, self.acc, self.instructions[self.IP][0], self.instructions[self.IP][1])
            if self.instructions[self.IP][0] == "nop":
                self.do_nop(self.instructions[self.IP][1])
            elif self.instructions[self.IP][0] == "acc":
                self.do_acc(self.instructions[self.IP][1])
            elif self.instructions[self.IP][0] == "jmp":
                self.do_jmp(self.instructions[self.IP][1])
            if self.IP in self.visited:
                return (False, self.acc)
            elif self.IP >= len(self.instructions):
                return (True, self.acc)
            self.visited.append(self.IP)
    def mutate_and_run(self):
        for changing, instruction in enumerate(self.instructions):
            if instruction[0] == 'jmp' or instruction[0] == 'nop':
                print "Changing instruction %d (%s)" % (changing, instruction)
                oldinstr = instruction[0]
                if instruction[0] == 'jmp':
                    instruction[0] = 'nop'
                elif instruction[0] == 'nop':
                    instruction[0] = 'jmp'
                completed, acc = self.run()
                if completed:
                    return acc
                instruction[0] = oldinstr
        return "I am a failure"
    def __repr__(self):
        return repr(self.instructions)


if __name__ == "__main__":
    with open('day08.txt', 'r') as f:
        inputdata = f.read().splitlines()
    c = computer(inputdata)
    print c.mutate_and_run()