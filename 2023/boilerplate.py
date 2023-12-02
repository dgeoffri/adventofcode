#!/usr/bin/env python3

import sys

DAY = 1
USE_SAMPLE_DATA = True
SAMPLE_DATA = """

"""

def solve_pt1(inputfile):
    print("Not implemented yet")

def solve_pt2(inputfile):
    print("Not implemented yet")

if __name__ == "__main__":
    if USE_SAMPLE_DATA:
        from io import StringIO
        puzzle_input = StringIO(SAMPLE_DATA)
    else:
        try:
            puzzle_input = open("day{:02d}.txt".format(DAY), "r")
        except OSError as e:
            print("Something went horribly wrong: {}".format(e))
            sys.exit(1)

    with puzzle_input as f:
        f.read()
        print("---PART 1---")
        solve_pt1(f)
        f.seek(0)
        print("---PART 2---")
        solve_pt2(f)
