#!/usr/bin/env python3

class Sub(object):
    def __init__(self):
        self.position = 0
        self.depth = 0
        self.aim = 0
    def executeCommand(self, command):
        direction, amount = (command[0], int(command[1]))
        print("Command: {}".format(command))
        if direction == "forward":
            self.position += amount
            self.depth += (self.aim * amount)
        elif direction == "up":
            self.aim -= amount
        elif direction == "down":
            self.aim += amount
        else:
            raise ValueError("Unrecognized command")

if __name__ == "__main__":
    with open('day02.txt', 'r') as inputfile:
         inputdata = [ tuple(line.split()) for line in inputfile.read().splitlines() ]
    mySub = Sub()
    for command in inputdata:
        mySub.executeCommand(command)
    print("Final horizontal position: {}, final depth: {}\nProduct of hpos * depth = {}".format(mySub.position, mySub.depth, mySub.position * mySub.depth))
