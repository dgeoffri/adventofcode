#!/usr/bin/env python3


class Reservoir:
    def __init__(self, puzzledata):
        self.rocks = set()
        self.sand = set()
        for line in puzzledata:
            coordinatelist = line.split(" -> ")
            start_coordinate = tuple(map(int, coordinatelist.pop(0).split(',')))
            while len(coordinatelist):
                end_coordinate = tuple(map(int, coordinatelist.pop(0).split(',')))
                if start_coordinate[0] == end_coordinate[0]:
                    x = start_coordinate[0]
                    y1 = start_coordinate[1]
                    y2 = end_coordinate[1]
                    if y1 > y2:
                        y1, y2 = y2, y1
                    for y in range(y1, y2 + 1):
                        self.rocks.add((x, y))
                elif start_coordinate[1] == end_coordinate[1]:
                    y = start_coordinate[1]
                    x1 = start_coordinate[0]
                    x2 = end_coordinate[0]
                    if x1 > x2:
                        x1, x2 = x2, x1
                    for x in range(x1, x2 + 1):
                        self.rocks.add((x, y))
                else:
                    raise ValueError("Can only draw straight lines!")
                start_coordinate = end_coordinate
        self.abyss_line = max(y for x, y in self.rocks)

    def drop_sand(self):
        new_sand_x, new_sand_y = (500, 0)
        at_rest = False
        while not at_rest:
            if new_sand_y > self.abyss_line:
                return False
            if (new_sand_x, new_sand_y + 1) not in self.sand | self.rocks:
                new_sand_y += 1
            elif (new_sand_x - 1, new_sand_y + 1) not in self.sand | self.rocks:
                new_sand_x -= 1
                new_sand_y += 1
            elif (new_sand_x + 1, new_sand_y + 1) not in self.sand | self.rocks:
                new_sand_x += 1
                new_sand_y += 1
            else:
                at_rest = True
        self.sand.add((new_sand_x, new_sand_y))
        return True


if __name__ == "__main__":
    # from io import StringIO

    # puzzle_input = StringIO(
    #     "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9")
    puzzle_input = open("day14.txt", "r")
    with puzzle_input as f:
        rock_structures = f.read().splitlines()
    r = Reservoir(rock_structures)
    while r.drop_sand():
        pass
    print(f"You can drop {len(r.sand)} units of sand before they begin to fall into the abyss.")
