#!/usr/bin/env python3

import sys
from collections import namedtuple

DAY = 5
USE_SAMPLE_DATA = False
SAMPLE_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

def readfile(infile):
    seeds = []
    maps = {}
    current_map = None
    Rangemap = namedtuple("Rangemap", "drstart srstart rangelength")
    for line in infile:
        line = line.rstrip()
        if len(line):
            if line.startswith("seeds:"):
                _, rest = line.split("seeds:")
                seeds = list(map(int, rest.split()))
            elif line.endswith("map:"):
                current_map, _ = line.split(maxsplit=1)
            else:
                r = Rangemap(*map(int, line.split()))
                try:
                    maps[current_map].append(r)
                except KeyError:
                    maps[current_map] = [r]
    return seeds, maps


def solve_pt1(inputfile):
    seeds, maps = readfile(inputfile)
    locations = []
    for seed in seeds:
        print(f"Seed {seed}:")
        for mapname in ("seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"):
            for rangemap in maps[mapname]:
                if seed in range(rangemap.srstart, rangemap.srstart + rangemap.rangelength):
                    print(f"mapping {seed} to {seed - rangemap.srstart + rangemap.drstart} because of rule {rangemap} in {mapname}")
                    seed = seed - rangemap.srstart + rangemap.drstart
                    break
        locations.append(seed)
    print(f"Lowest location is {min(locations)}")

def solve_pt2(inputfile):
    seeds, maps = readfile(inputfile)
    lowest = None
    while len(seeds):
    # for _ in (1,):
        startseed = seeds.pop(0)
        seedrange = seeds.pop(0)
        # startseed = 443681800
        # seedrange = 544174761
        print(f"Checking seeds {startseed} through {startseed + seedrange}")
        for seed in range(startseed, startseed + seedrange, 100):
            seedboy = seed
            # print(f"Seed {seed}:")
            for mapname in ("seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"):
                for rangemap in maps[mapname]:
                    if seed in range(rangemap.srstart, rangemap.srstart + rangemap.rangelength):
                        # print(f"mapping {seed} to {seed - rangemap.srstart + rangemap.drstart} because of rule {rangemap} in {mapname}")
                        seed = seed - rangemap.srstart + rangemap.drstart
                        break
            if lowest == None:
                lowest = seed
            else:
                if seed < lowest:
                    lowest = seed
                    print(f"new low of {seed} found with seedboy {seedboy}")
    print(f"Lowest location is {lowest}")

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