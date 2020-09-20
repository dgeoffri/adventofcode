#!/usr/bin/env python

import re
validate=re.compile("[+-]?\d+")
if hasattr(__builtins__, 'raw_input'):
    input = raw_input
inputline=input("Enter frequency offset: ")
while not validate.match(inputline):
	inputline=input("Invalid entry.  Enter frequency offset: ")
sum=int(inputline)
while inputline != "":
	inputline=input("Enter frequency offset: ")
	if inputline=="": break
	while not validate.match(inputline):
		inputline=input("Invalid entry.  Enter frequency offset: ")
	sum += int(inputline)
print("The sum is "+str(sum))
