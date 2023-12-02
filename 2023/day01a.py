#!/usr/bin/env python3

USE_SAMPLE_DATA = True

if __name__ == "__main__":
    if USE_SAMPLE_DATA:
        from io import StringIO
        puzzle_input = StringIO("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet")
    else:
        puzzle_input = open("day01.txt", "r")

    running_total = 0
    with puzzle_input as f:
        for line in f:
            numbers_in_line = tuple(map(int, filter(lambda x: x.isnumeric(), line.strip())))
            running_total += (numbers_in_line[0] * 10) + numbers_in_line[-1]
    print(f"Total is {running_total}")
