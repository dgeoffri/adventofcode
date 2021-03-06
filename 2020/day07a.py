#!/usr/bin/env python

import re

def contains_gold(bags, bag):
    if "shiny gold" in [y for _, y in bags[bag]]:
        return True
    for _, y in bags[bag]:
        if contains_gold(bags, y):
            return True
    return False


if __name__ == "__main__":
    with open('day07.txt', 'r') as f:
        inputdata = f.read().splitlines()
    re1 = re.compile(r"(\w+ \w+) bags contain (.*)")
    re2 = re.compile(r"(\d+) (\w+ \w+) bag[s]?")
    bags = {}
    for line in inputdata:
        tmp = re1.findall(line)
        bags[tmp[0][0]] = re2.findall(tmp[0][1])
    print "{} bags eventually contain a shiny gold bag".format(len(filter(lambda x: contains_gold(bags, x), bags.keys())))
