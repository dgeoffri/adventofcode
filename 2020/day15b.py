#!/usr/bin/env python

if __name__ == "__main__":
    # with open('day13.txt', 'r') as f:
    z = [6, 4, 12, 1, 20, 0, 16]
    z.reverse()
    for _ in xrange(30000000 - len(z)):
        try:
            z.insert(0, z[1:].index(z[0]) + 1)
        except ValueError:
            z.insert(0, 0)
        print z
