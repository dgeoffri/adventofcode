#!/usr/bin/env python3

USE_SAMPLE_DATA = False
numbernames = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def findnumbers(inputline: str) -> tuple:
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

if __name__ == "__main__":
    if USE_SAMPLE_DATA:
        from io import StringIO
        puzzle_input = StringIO("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen")
    else:
        puzzle_input = open("day01.txt", "r")
    running_total = 0
    with puzzle_input as f:
        for line in f:
            numbers_in_line = findnumbers(line.strip())
            calibration_value = (numbers_in_line[0] * 10) + numbers_in_line[-1]
            running_total += calibration_value
            print(f"{line.strip()} -- {numbers_in_line} -- calibration value: {calibration_value}")
    print(f"Total is {running_total}")
