#!/usr/bin/env python3

import sys
import math

DAY = 8
USE_SAMPLE_DATA = False
SAMPLE_DATA = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

SAMPLE_DATA = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


def parse_input(inputfile):
    directions = inputfile.readline().strip()
    inputfile.readline()
    rooms = {}
    for line in inputfile:
        room, paths = line.strip().split(" = ")
        paths = tuple(paths.strip(")(").split(", "))
        rooms[room] = paths
    return directions, rooms


def solve_pt1(inputfile):
    directions, rooms = parse_input(inputfile)
    directions_len = len(directions)
    # print(directions, rooms)
    moves = 0
    current_room = rooms["AAA"]
    while current_room != rooms["ZZZ"]:
        go = directions[moves % directions_len]  # L or R
        current_room = rooms[current_room["LR".index(go)]]
        moves += 1
    print(moves)


def solve_pt2(inputfile):
    directions, rooms = parse_input(inputfile)
    directions_len = len(directions)
    # print(directions, rooms)
    current_rooms = [room for room in rooms if room.endswith("A")]

    intervals = []
    for room in current_rooms:
        moves = 0
        current_room = room
        while not current_room.endswith("Z"):
            go = directions[moves % directions_len]  # L or R
            current_room = rooms[current_room]["LR".index(go)]
            moves += 1
        intervals.append(moves)
    print(f"Moves: {math.lcm(*intervals)}")


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
