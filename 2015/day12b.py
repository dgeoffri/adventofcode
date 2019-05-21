#!/usr/bin/env python
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
    
def recurse_no_red(data):
    total = 0
    if isinstance(data, dict):
        for i in data.values():
            if i == u'red':
                return 0
            else:
                total += recurse_no_red(i)
    elif isinstance(data, (tuple, list)):
        for i in data:
            total += recurse_no_red(i)
    elif isinstance(data, int):
        total += data
    return total

with open('day12.txt', 'r') as inputfile:
	j = json.loads(inputfile.read())
	print "Counting all the numbers, the result is:", recurse(j)
	print "Counting all the numbers, excluding any object and its children if it contains a red item, the result is:", recurse_no_red(j)
