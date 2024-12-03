#!/usr/bin/env python3

import sys, re

DAY = 3
SAMPLE_DATA = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

def solve_pt1(inputfile):
    matcher = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    data = inputfile.read()
    matches = matcher.findall(data)
    total = 0
    for match in matches:
        a, b = map(int, match)
        z = a * b
        # print(f"{a} * {b} = {z}")
        total += z
    print(f"Sum of instruction results = {total}")

def solve_pt2(inputfile):
    matcher = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    data = inputfile.read()
    data = re.split(r"don't\(\)", data)
    reconstituted = data.pop(0)
    for segment in data:
        parts = re.split(r"do\(\)", segment)
        if len(parts) > 1:
            reconstituted += ''.join(parts[1:])
    data = reconstituted
    matches = matcher.findall(data)
    total = 0
    for match in matches:
        a, b = map(int, match)
        z = a * b
        # print(f"{a} * {b} = {z}")
        total += z
    print(f"Sum of instruction results = {total}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-e":
        from io import StringIO
        puzzle_input = StringIO(SAMPLE_DATA)
    else:
        try:
            puzzle_input = open("day{:02d}.txt".format(DAY), "r")
        except OSError as e:
            print("Something went horribly wrong: {}".format(e))
            sys.exit(1)

    with puzzle_input as f:
        print("---PART 1---")
        solve_pt1(f)
        f.seek(0)
        print("\n---PART 2---")
        solve_pt2(f)
