#!/usr/bin/env python3

import sys

DAY = 1
USE_SAMPLE_DATA = False
SAMPLE_DATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def findnumbers(inputline: str) -> tuple:
    numbernames = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_so_far = []
    while len(inputline):
        for numbertocheck in numbernames:
            if inputline.startswith(numbertocheck):
                numbers_so_far.append(numbernames.index(numbertocheck))
                inputline = inputline[1:]
                break
        else:
            if inputline[0].isnumeric():
                numbers_so_far.append(int(inputline[0]))
            inputline = inputline[1:]
    return tuple(numbers_so_far)

def solve_pt1(inputfile):
    running_total = 0
    for line in inputfile:
        numbers_in_line = tuple(map(int, filter(lambda x: x.isnumeric(), line.strip())))
        running_total += (numbers_in_line[0] * 10) + numbers_in_line[-1]
    print(f"Total is {running_total}")

def solve_pt2(inputfile):
    running_total = 0
    for line in f:
        numbers_in_line = findnumbers(line.strip())
        calibration_value = (numbers_in_line[0] * 10) + numbers_in_line[-1]
        running_total += calibration_value
        # print(f"{line.strip()} -- {numbers_in_line} -- calibration value: {calibration_value}")
    print(f"Total is {running_total}")

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
        print("---PART 1---")
        solve_pt1(f)
        f.seek(0)
        print("\n---PART 2---")
        solve_pt2(f)
