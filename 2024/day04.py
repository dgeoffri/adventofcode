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
                    if (xcursor + (xdir * (wordlen - 1))) < 0 or (xcursor + (xdir * (wordlen - 1))) >= width or (ycursor + (ydir * (wordlen - 1))) < 0 or (ycursor + (ydir * (wordlen - 1))) >= height:
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
    SUB_WORD_TO_FIND = WORD_TO_FIND[1:]
    print(SUB_WORD_TO_FIND)
    assert len(SUB_WORD_TO_FIND) == 3
    count = 0
    puzzle = []
    for line in inputfile:
        puzzle.append(list(line.rstrip()))
    for line in puzzle:
        print(' '.join(line))
    width = len(puzzle[0])
    height = len(puzzle)
    for ycursor in range(1, height - 1):
        for xcursor in range(1, width - 1):
            count_at_cursor = 0
            for xdir, ydir in (1, 1), (1, -1), (-1, 1), (-1, -1):
                xstart, ystart = xcursor - xdir, ycursor - ydir
                if (xstart + (xdir * 2)) < 0 or (xstart + (xdir * 2)) >= width or (ystart + (ydir * 2)) < 0 or (ystart + (ydir * 2)) >= height:
                    continue
                for position, letter in enumerate(SUB_WORD_TO_FIND):
                    print(f"checking position {xstart + (xdir * position)},{ystart + (ydir * position)} for the letter {letter}")
                    if puzzle[ystart + (ydir * position)][xstart + (xdir * position)] != letter:
                        break
                else:
                    print(f"FOUND {SUB_WORD_TO_FIND} at {xstart}, {ystart} with xdir={xdir} and ydir={ydir}")
                    count_at_cursor += 1
            if count_at_cursor > 1:
                print(f"FOUND {SUB_WORD_TO_FIND} criss-crossed at {xcursor}, {ycursor}!")
                count += 1
    print(f"Found the word {SUB_WORD_TO_FIND} criss-crossed {count} times in the puzzle!")

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
