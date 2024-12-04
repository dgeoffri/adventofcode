#!/usr/bin/env python3

import sys

DAY = 4
SAMPLE_DATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
WORD_TO_FIND = "XMAS"

def solve_pt1(inputfile):
    count = 0
    puzzle = []
    for line in inputfile:
        puzzle.append(list(line.rstrip()))
    for line in puzzle:
        print(' '.join(line))
    width = len(puzzle[0])
    height = len(puzzle)
    wordlen = len(WORD_TO_FIND)
    for ycursor in range(height):
        for xcursor in range(width):
            for xdir in (1, 0, -1):
                for ydir in (-1, 0, 1):
                    if xdir == ydir == 0:
                        continue
                    if (xcursor + (xdir * wordlen)) < 0 or (xcursor + (xdir * wordlen)) > width or (ycursor + (ydir * wordlen)) < 0 or (ycursor + (ydir * wordlen)) > height:
                        continue
                    for position, letter in enumerate(WORD_TO_FIND):
                        print(f"checking position {xcursor + (xdir * position)},{ycursor + (ydir * position)} for the letter {letter}")
                        if puzzle[ycursor + (ydir * position)][xcursor + (xdir * position)] != letter:
                            break
                    else:
                        print(f"FOUND {WORD_TO_FIND} at {xcursor}, {ycursor} with xdir={xdir} and ydir={ydir}")
                        count += 1
    print(f"Found the word {WORD_TO_FIND} {count} times in the puzzle!")
    

def solve_pt2(inputfile):
    print("Not implemented yet")

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
