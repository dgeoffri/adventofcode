#!/usr/bin/env python

if __name__ == "__main__":
    inputdata = open("day02.txt", "r").read().splitlines()
    validpasswords = []
    for line in inputdata:
        policy, password = line.split(": ")
        minmax, letter = policy.split()
        mincount, maxcount = map(int, minmax.split("-"))
        if (password.count(letter) >= mincount) and (password.count(letter) <= maxcount):
            validpasswords.append(password)

    print "%d valid passwords found" % len(validpasswords)
