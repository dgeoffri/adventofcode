#!/usr/bin/env python

import sys

txt = open(sys.argv[1], 'r').read()

x = txt.count('(')
y = txt.count(')')

print (x) 
print (y) 
print (x-y)
