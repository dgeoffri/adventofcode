#!/usr/bin/python
# coding: utf-8

import json

def recurse(data):
    total = 0
    if isinstance(data, dict):
        for i in data.values():
            total += recurse(i)
    elif isinstance(data, (tuple, list)):
        for i in data:
            total += recurse(i)
    elif isinstance(data, int):
        total += data
    return total

with open('day12.txt', 'r') as inputfile:
	j = json.loads(inputfile.read())
	print "Counting all the numbers, the result is:", recurse(j)
