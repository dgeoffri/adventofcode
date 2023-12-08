#!/usr/bin/env python3

import sys
from functools import reduce
import operator

DAY = 6
USE_SAMPLE_DATA = False
SAMPLE_DATA = """Time:      7  15   30
Distance:  9  40  200
"""


def solve_pt1(inputfile):
    _, times = inputfile.readline().strip().split(maxsplit=1)
    times = list(map(int, times.split()))
    _, distances = inputfile.readline().strip().split(maxsplit=1)
    distances = list(map(int, distances.split()))

    ways_to_win = []
    for race in range(len(times)):
        winning_durations = []
        for holdtime in range(1, times[race]):
            distance = (times[race] - holdtime) * holdtime
            if distance > distances[race]:
                winning_durations.append(holdtime)
        ways_to_win.append(len(winning_durations))
    print(f"Answer: {reduce(operator.mul, ways_to_win, 1)}")

def solve_pt2(inputfile):
    _, time = inputfile.readline().strip().split(maxsplit=1)
    time = int(''.join(time.split()))
    _, record = inputfile.readline().strip().split(maxsplit=1)
    record = int(''.join(record.split()))

    mintime = 0
    maxtime = 0
    for holdtime in range(1, time):
        distance = (time - holdtime) * holdtime
        if not mintime and distance > record:
            mintime = holdtime
            continue
        if mintime and not maxtime and distance <= record:
            maxtime = holdtime
            break
    print(f"{maxtime - mintime} ways to win")


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
