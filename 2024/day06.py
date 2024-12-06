#!/usr/bin/env python3

import sys

DAY = 6
SAMPLE_DATA = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

def solve_pt1(inputfile):
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
    obstacles = set()
    visited = set()
    guard = ()
    for y, line in enumerate(inputfile):
        line = line.strip()
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                guard = (x, y)
        width = x +1
    height = y + 1
    print(f"Guard is at {guard}")
    visited.add(guard)
    next_step = (guard[0] + DIRECTIONS[0][0], guard[1] + DIRECTIONS[0][1])
    while (-1 < next_step[0] < width) and (-1 < next_step[1] < height):
        if next_step in obstacles:
            DIRECTIONS.append(DIRECTIONS.pop(0))
            next_step = (guard[0] + DIRECTIONS[0][0], guard[1] + DIRECTIONS[0][1])
            continue
        guard = next_step
        visited.add(guard)
        print(f"Guard is at {guard}")
        next_step = (guard[0] + DIRECTIONS[0][0], guard[1] + DIRECTIONS[0][1])
    print(visited)
    print(f"Guard visited {len(visited)} distinct spaces before wandering off of the map")

def solve_pt2(inputfile):
    obstacles = set()
    obstacle_locations_to_cause_looping = set()
    guard_start = ()
    for y, line in enumerate(inputfile):
        line = line.strip()
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                guard_start = (x, y)
        width = x +1
    height = y + 1
    guard = guard_start
    for y in range(height):
        for x in range(width):
            if (x, y) == guard_start:
                continue
            DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
            visited = set()
            obstacles2 = obstacles.copy()
            obstacles2.add((x, y))
            guard = guard_start
            # print(f"Guard is at {guard}, facing {DIRECTIONS[0]}")
            visited.add((guard, DIRECTIONS[0]))
            next_step = (guard[0] + DIRECTIONS[0][0], guard[1] + DIRECTIONS[0][1])
            stuck_in_loop = False
            while (-1 < next_step[0] < width) and (-1 < next_step[1] < height):
                if (next_step, DIRECTIONS[0]) in visited:
                    stuck_in_loop = True
                    break
                if next_step in obstacles2:
                    DIRECTIONS.append(DIRECTIONS.pop(0))
                    next_step = (guard[0] + DIRECTIONS[0][0], guard[1] + DIRECTIONS[0][1])
                    continue
                guard = next_step
                visited.add((guard, DIRECTIONS[0]))
                # print(f"Guard is at {guard}, facing {DIRECTIONS[0]}")
                next_step = (guard[0] + DIRECTIONS[0][0], guard[1] + DIRECTIONS[0][1])
            if stuck_in_loop:
                # print(f"Guard got stuck in a loop!")
                obstacle_locations_to_cause_looping.add((x, y))
            else:
                # print(f"Guard wandered off the map without getting stuck in a loop")
                pass
    print(f"There are {len(obstacle_locations_to_cause_looping)} locations that would cause looping:")
    print(obstacle_locations_to_cause_looping)


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
