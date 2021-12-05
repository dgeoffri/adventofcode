#!/usr/bin/env python3

def get_gamma_rate(the_input):
    return idk(the_input, 0)

def get_epsilon_rate(the_input):
    return idk(the_input, -1)

def get_oxygen_generator_rating(the_input):
    return idk(the_input, 0, True)

def get_co2_scrubber_rating(the_input):
    return idk(the_input, -1, True)

def idk(the_input, position, buildstrfilter = False):
    buildstr = ''
    if buildstrfilter:
        filterfunc = lambda x: x.startswith(buildstr)
    else:
        filterfunc = lambda x: True
    for x in range(len(inputdata[0])):
        the_digit = [ y[x] for y in filter(filterfunc, inputdata) ]
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
    oxygen_generator_rating = int(get_oxygen_generator_rating(inputdata), 2)
    co2_scrubber_rating = int(get_co2_scrubber_rating(inputdata), 2)
    print("gamma rate:              {}".format(gamma_rate))
    print("epsilon rate:            {}".format(epsilon_rate))
    print("power consumption:       {}".format(gamma_rate * epsilon_rate))
    print("oxygen generator rating: {}".format(oxygen_generator_rating))
    print("co2 scrubber rating:     {}".format(co2_scrubber_rating))
    print("life support rating:     {}".format(oxygen_generator_rating * co2_scrubber_rating))
