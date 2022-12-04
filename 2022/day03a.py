#!/usr/bin/env python3

PRIORITIES = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def outgrabe(first, second):
    for i in first:
        if i in second:
            return PRIORITIES.index(i)
            
if __name__ == "__main__":
    with open("day03.txt", "r") as fp:
        data = fp.read().splitlines()
    total = 0
    for line in data:
        linelen = len(line)
        first, second = line[linelen//2:], line[:linelen//2]
        total += outgrabe(first, second)
    print(f"Sum of the priorities is: {total}")

