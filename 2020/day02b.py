#!/usr/bin/env python

if __name__ == "__main__":
    inputdata = open("day02.txt", "r").read().splitlines()
    validpasswords = []
    for line in inputdata:
        policy, password = line.split(": ")
        minmax, letter = policy.split()
        firstpos, secondpos = map(int, minmax.split("-"))
        if (password[firstpos-1] == letter) ^ (password[secondpos-1] == letter):
            validpasswords.append(password)

    print "%d valid passwords found" % len(validpasswords)
