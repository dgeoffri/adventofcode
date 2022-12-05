#!/usr/bin/env python3

class SectionRange:
    def __init__(self, i):
        numbers = map(int, i.split("-"))
        self.lower, self.higher = sorted(numbers)

    def contains(self, other):
        return (other.lower >= self.lower) and (other.higher <= self.higher)

    def __repr__(self):
        return f"[ {self.lower} - {self.higher} ]"

if __name__ == "__main__":
    with open("day04.txt", "r") as fp:
        data = fp.read().splitlines()
    contained_ranges = 0
    for pair in data:
        elves = tuple(map(SectionRange, pair.split(",")))
        if elves[0].contains(elves[1]) or elves[1].contains(elves[0]):
            contained_ranges += 1
    print(f"{contained_ranges} ranges are fully contained by a partner's range.")
