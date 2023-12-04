#!/usr/bin/env python3

import sys

DAY = 3
USE_SAMPLE_DATA = False
SAMPLE_DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def create_floormap(inputfile):
    floormap = []
    line_width = None
    for line in inputfile:
        line = line.strip()
        floormap.append(line)
        if line_width == None:
            line_width = len(line)
        else:
            assert (len(line) == line_width)
    return floormap


def solve_pt1(inputfile):
    floormap = create_floormap(inputfile)
    height = len(floormap)
    width = len(floormap[0])

    def check_symbol_adjacency(row_number, column_range):
        column_start, column_end = column_range
        # Check line above if inside map
        if (row_number - 1) >= 0:
            for column_number in range(max(column_start - 1, 0), min((column_end + 1) + 1, width)):
                t = floormap[row_number - 1][column_number]
                if t != "." and not t.isnumeric():
                    return True
        # Check points to each side
        for column_number in (column_start - 1, column_end + 1):
            if width > column_number >= 0:
                t = floormap[row_number][column_number]
                if t != "." and not t.isnumeric():
                    return True
        # Check line above if inside map
        if (row_number + 1) < height:
            for column_number in range(max(column_start - 1, 0), min((column_end + 1) + 1, width)):
                t = floormap[row_number + 1][column_number]
                if t != "." and not t.isnumeric():
                    return True
        return False
    numbers = []
    for row_number, row in enumerate(floormap):
        number_columnranges = []
        start = None
        for column_number, value in enumerate(row):
            if start is not None:
                if value.isnumeric():
                    continue
                else:
                    number_columnranges.append((start, column_number - 1))
                    start = None
            elif value.isnumeric():
                start = column_number
        if value.isnumeric():
            if start is not None:
                number_columnranges.append((start, column_number))
            else:
                number_columnranges.append((column_number, column_number))
        numbers += [int(row[start:end+1]) for start, end in number_columnranges if check_symbol_adjacency(row_number, (start, end))]

    # print(f"Part numbers: {numbers}")
    print(f"Total:        {sum(numbers)}")

def solve_pt2(inputfile):
    floormap = create_floormap(inputfile)
    height = len(floormap)
    width = len(floormap[0])

    def check_gear_adjacency(row_number, column_range):
        column_start, column_end = column_range
        adjacent_gears = []
        # Check line above if inside map
        if (row_number - 1) >= 0:
            for column_number in range(max(column_start - 1, 0), min((column_end + 1) + 1, width)):
                t = floormap[row_number - 1][column_number]
                if t == "*":
                    adjacent_gears.append((row_number - 1, column_number))
        # Check points to each side
        for column_number in (column_start - 1, column_end + 1):
            if width > column_number >= 0:
                t = floormap[row_number][column_number]
                if t == "*":
                    adjacent_gears.append((row_number, column_number))
        # Check line above if inside map
        if (row_number + 1) < height:
            for column_number in range(max(column_start - 1, 0), min((column_end + 1) + 1, width)):
                t = floormap[row_number + 1][column_number]
                if t == "*":
                    adjacent_gears.append((row_number + 1, column_number))
        return adjacent_gears
    gears_touching_numbers = {}
    for row_number, row in enumerate(floormap):
        number_columnranges = []
        start = None
        for column_number, value in enumerate(row):
            if start is not None:
                if value.isnumeric():
                    continue
                else:
                    number_columnranges.append((start, column_number - 1))
                    start = None
            elif value.isnumeric():
                start = column_number
        if value.isnumeric():
            if start is not None:
                number_columnranges.append((start, column_number))
            else:
                number_columnranges.append((column_number, column_number))
        for number_columnrange in number_columnranges:
            gears = check_gear_adjacency(row_number, number_columnrange)
            for gear in gears:
                column_start, column_end = number_columnrange
                number = int(row[column_start:column_end+1])
                # print(f"Found gear at {gear} touching number {number}")
                try:
                    gears_touching_numbers[gear].append(number)
                except KeyError:
                    gears_touching_numbers[gear] = [number]
    gears_touching_numbers = { k:v for k, v in gears_touching_numbers.items() if len(v) == 2 }
    gear_ratios = [ num1 * num2 for num1, num2 in gears_touching_numbers.values() ]

    print(f"Total:        {sum(gear_ratios)}")

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
