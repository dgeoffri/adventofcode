#!/usr/bin/env python
# coding: utf-8
import re

regex=re.compile(r'(.+): (.+) (-?\d+), (.+) (-?\d+), (.+) (-?\d+), (.+) (-?\d+), (.+) (-?\d+)$'); 
try:
	inputdata=open('day15.txt', 'r').read().splitlines()
except Exception:
	print "I had some issue reading the input data"

ingredients = dict()

for line in inputdata:
    data = regex.match(line).groups()
    ingredients[data[0]] = { data[1]: int(data[2]), data[3]: int(data[4]), data[5]: int(data[6]), data[7]: int(data[8]), data[9]: int(data[10]) }
del inputdata

print ingredients
