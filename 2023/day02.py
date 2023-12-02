#!/usr/bin/env python3

import sys

DAY = 2
USE_SAMPLE_DATA = False
SAMPLE_DATA = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def solve_pt1(inputfile):
    CUBES = {"red": 12, "green": 13, "blue": 14}
    possible_games = []
    for line in inputfile:
        game_number, game_data = line.strip().split(": ")
        game_number = int(game_number.split(" ")[-1])
        for cubeset in game_data.split("; "):
            cs = {i.split(" ")[1]: int(i.split(" ")[0]) for i in cubeset.split(", ")}
            possible = True
            for color in cs:
                if cs[color] > CUBES[color]:
                    possible = False
                    break
            if not possible:
                break
        else:
            possible_games.append(game_number)
    print(f"Sum of IDs of possible games: {sum(possible_games)}")

def solve_pt2(inputfile):
    from functools import reduce
    import operator
    game_powers = []
    for line in inputfile:
        game_number, game_data = line.strip().split(": ")
        game_number = int(game_number.split(" ")[-1])
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for cubeset in game_data.split("; "):
            cs = {i.split(" ")[1]: int(i.split(" ")[0]) for i in cubeset.split(", ")}
            for color in cs:
                if cs[color] > min_cubes[color]:
                    min_cubes[color] = cs[color]
        # game_powers.append(min_cubes["red"] * min_cubes["green"] * min_cubes["blue"])
        game_powers.append(reduce(operator.mul, min_cubes.values()))
    print(f"Sum of powers of all games: {sum(game_powers)}")

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
