#!/usr/bin/python
# coding: utf-8

def lookandsay(number, maxiterations):
        for n in xrange(maxiterations):
		temp = list()
		for i in str(number):
			if len(temp) > 0 and int(i) == temp[-1][1]:
				temp[-1][0] += 1
			else:
				temp.append([1,int(i)])
		number = ''.join([''.join(map(str,i)) for i in temp])
	return number

num = lookandsay(3113322113, 40)

print "The length at the 40th iteration is", len(num)

num = lookandsay(num, 10)

print "The length at the 50th iteration is", len(num)
