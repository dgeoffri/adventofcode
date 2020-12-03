#!/usr/bin/env python

if __name__ == "__main__":
    with open('day02.txt', 'r') as f:
        inputdata = f.read().splitlines()
    validpasswords = []
    for line in inputdata:
        policy, password = line.split(": ")
        minmax, letter = policy.split()
        firstpos, secondpos = map(int, minmax.split("-"))
        if (password[firstpos-1] == letter) ^ (password[secondpos-1] == letter):
            validpasswords.append(password)

    print "%d valid passwords found" % len(validpasswords)
