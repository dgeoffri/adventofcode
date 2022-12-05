#!/usr/bin/env python3

class SectionRange:
    def __init__(self, i):
        numbers = map(int, i.split("-"))
        self.lower, self.higher = sorted(numbers)

    def contains(self, other):
        return (other.lower >= self.lower) and (other.higher <= self.higher)

    def overlaps(self, other):
        return other.lower in range(self.lower, self.higher + 1) or \
            other.higher in range(self.lower, self.higher + 1) or \
            self.lower in range(other.lower, other.higher + 1) or \
            self.higher in range(other.lower, other.higher + 1)

    def __repr__(self):
        return f"[ {self.lower} - {self.higher} ]"


if __name__ == "__main__":
    with open("day04.txt", "r") as fp:
        data = fp.read().splitlines()
    overlapping_ranges = 0
    for pair in data:
        elves = tuple(map(SectionRange, pair.split(",")))
        if elves[0].overlaps(elves[1]):
            overlapping_ranges += 1
    print(f"{overlapping_ranges} ranges somewhat overlap those of a partner's.")
