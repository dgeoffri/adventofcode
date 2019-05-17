#!/usr/bin/env python

import sys

class Password(object):
    def __init__(self, startpassword='a'):
        self.password = startpassword
    def next(self):
        newpass = str()
        inc = True
        for i in reversed(self.password):
            if inc:
                i = chr(ord(i) + 1)
                if i > 'z':
                    i = 'a'
                else:
                    inc = False
            newpass += i
        self.password = ''.join(reversed(newpass))
        return self
    def validate(self):
        lastchar = ''
        straightNeeded = 2
        doublesNeeded = 2
        justDoubled = False
        for i in self.password:
            if i in 'iol':
                return False
            if straightNeeded:
                if len(lastchar) and ord(i) == (ord(lastchar) + 1):
                    straightNeeded -= 1
                else:
                   straightNeeded = 2
            if not justDoubled and i == lastchar:
                doublesNeeded -= 1
                justDoubled = True
            else:
                justDoubled = False
            lastchar = i
        return (not straightNeeded and not doublesNeeded)
    def nextValid(self):
        self.next()
        while not self.validate():
            self.next()
        return self
        
if len(sys.argv) != 2:
    print "Usage: %s <current password>\n\nReturns the next 2 valid passwords for Santa that follow his own rotation system and comply with the minimum password strength requirements" % sys.argv[0]
    sys.exit(1)

password = Password(sys.argv[1]).nextValid()
print "The next valid password for Santa is", password.password

