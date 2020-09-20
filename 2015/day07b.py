#!/usr/bin/env python

for _ in (0,1):    
    with open('day07.txt', 'r') as inputfile:
            b=[ [ i.split(' -> ')[0].split(' '), i.split(' -> ')[1] ] for i in inputfile.read().splitlines() ]
            wiredict = {}
            for i in b:
		for j in xrange(len(i[0])):
                        if i[0][j].isdigit():
                                i[0][j]=int(i[0][j])
                if (i[1] == 'b') and ('a' in vars()):
                    print "Overriding wire b with signal", a, "and resetting" 
                    i[0] = [a]
            while len(b):
                    temp = b.pop(0)
                    if len(temp[0]) == 1:
                            if type(temp[0][0]) is int:
                                    wiredict[temp[1]] = temp[0][0]
                            elif temp[0][0] in wiredict:
                                    wiredict[temp[1]] = wiredict[temp[0][0]]
                            else:
                                    b.append(temp)
                    elif len(temp[0]) == 2:
                            if temp[0][1] in wiredict:
                                    wiredict[temp[1]] = 65535 ^ wiredict[temp[0][1]]
                            else:
                                    b.append(temp)
                    elif len(temp[0]) == 3:
                            if ((temp[0][0] in wiredict) or (type(temp[0][0]) is int)) and ((temp[0][2] in wiredict) or (type(temp[0][2]) is int)):
                                    for n in (0, 2):
                                            if type(temp[0][n]) is not int:
                                                    temp[0][n] = wiredict[temp[0][n]]	
                                    if temp[0][1] == 'LSHIFT':
                                            wiredict[temp[1]] = temp[0][0] << temp[0][2]
                                    elif temp[0][1] == 'RSHIFT':
                                            wiredict[temp[1]] = temp[0][0] >> temp[0][2]
                                    elif temp[0][1] == 'AND':
                                            wiredict[temp[1]] = temp[0][0] & temp[0][2]
                                    elif temp[0][1] == 'OR':
                                            wiredict[temp[1]] = temp[0][0] | temp[0][2]
                            else:
                                    b.append(temp)
            a = wiredict['a']
            print "Wire a has a signal of", a
