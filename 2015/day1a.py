#!/usr/bin/env python

import sys

txt = sys.argv[1]

x = txt.count('(')
y = txt.count(')')

print (x) 
print (y) 
print (x-y)
