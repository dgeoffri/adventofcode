#!/usr/bin/env python

import sys

def iterate(recipes, elf1, elf2):
    sum = recipes[elf1]+recipes[elf2]
    for digit in str(sum):
        recipes.append(int(digit))
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    return elf1, elf2

recipes = [3, 7]
elf1 = 0
elf2 = 1
num = int(sys.argv[1])

for _ in xrange(num + 10):
    elf1, elf2 = iterate(recipes, elf1, elf2)

print "".join(map(str,recipes[num:num+10]))
