#!/usr/bin/env python3

def get_gamma_rate(the_input):
    return idk(the_input, 0)

def get_epsilon_rate(the_input):
    return idk(the_input, -1)

def idk(the_input, position):
    buildstr = ''
    for x in range(len(inputdata[0])):
        the_digit = [ y[x] for y in inputdata ]
        tallies = {}
        for possibility in set(the_digit):
            tallies[possibility] = the_digit.count(possibility)
        buildstr += sorted(tallies.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[position][0]
    return buildstr

if __name__ == "__main__":
    with open('day03.txt', 'r') as inputfile:
         inputdata = inputfile.read().splitlines()
    gamma_rate = int(get_gamma_rate(inputdata), 2)
    epsilon_rate = int(get_epsilon_rate(inputdata), 2)
    print("gamma rate:        {}".format(gamma_rate))
    print("epsilon rate:      {}".format(epsilon_rate))
    print("power consumption: {}".format(gamma_rate * epsilon_rate))
