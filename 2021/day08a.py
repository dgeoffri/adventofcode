#!/usr/bin/env python3

if __name__ == "__main__":
    with open("day08.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()
    rightsides = [ line.split("|")[1].split() for line in lines ]
    lit_segment_counts = [ list(map(len, display)) for display in rightsides ]
    count = len(list(filter(lambda x: x in map(int, "2347"), sum(lit_segment_counts, []))))
    print("The digit 1, 4, 7, or 8 occurs {} times.".format(count))
