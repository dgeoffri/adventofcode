#!/usr/bin/env python3

if __name__ == "__main__":
    with open("day07.txt", "r") as inputfile:
        positions = list(map(int, inputfile.read().strip().split(',')))
    highest = max(positions)
    z = [ (sum(map(lambda x: abs(x-n), positions)),n) for n in range(highest) ]
    fuel_cost, cheapest_position = min(z)
    print("Cheapest solution is to meet at position {}, for a fuel cost of {}.".format(cheapest_position, fuel_cost))
