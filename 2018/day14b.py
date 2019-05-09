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
num = [int(digit) for digit in sys.argv[1]]
oldlen = 0
matched = False

while not matched:
    oldlen = len(recipes)
    elf1, elf2 = iterate(recipes, elf1, elf2)
    # print recipes, oldlen, len(recipes)
    for i in xrange(len(recipes)-oldlen):
        if (recipes[-len(num)-i:len(recipes)-i] == num):
            matched = True
            print "matched after", len(recipes)-len(num)-i, "recipes"
            break

