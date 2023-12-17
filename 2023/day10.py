#!/usr/bin/env python3

import sys
from itertools import combinations

DAY = 10
USE_SAMPLE_DATA = False
SAMPLE_DATA = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""


class Maze:
    def __init__(self, inputfile):
        self._maze = [[PipeSegment(char) for char in line] for line in inputfile.read().splitlines()]
        for y, line in enumerate(self._maze):
            for x, segment in enumerate(line):
                if segment == PipeSegment("S"):
                    self.start = (x, y)
                    break
            else:
                continue
            break

    def __repr__(self):
        return "\n".join((''.join(map(str, line)) for line in self._maze))

    def __getitem__(self, item):
        if type(item) == tuple:
            return self._maze[item[1]][item[0]]
        else:
            return self._maze[item]


    def walk_around(self):
        pos = self.start
        came_from = None
        steps_taken = []
        # start off in the first direction available
        for i in ((0, -1, PipeSegment.S), (0, 1, PipeSegment.N), (1, 0, PipeSegment.W), (-1, 0, PipeSegment.E)):
            try:
                x, y = (sum(x) for x in zip(pos, i[:2]))
                needs_dir = i[2]
                if (x < 0) or (y < 0):
                    continue
                if self[x,y].can_go(needs_dir):
                    pos = (x, y)
                    came_from = needs_dir
                    break
            except IndexError:
                continue
        else:
            raise Exception("Can't find any path from start point")
        # follow pipes until Start is found again
        while pos != self.start:
            steps_taken.append(pos)
            direction = self[pos].where_next(came_from)
            came_from = PipeSegment.invert_direction(direction)
            pos = tuple(sum(x) for x in zip(pos, PipeSegment.dir_to_rel_coords(direction)))
        steps_taken.append(pos)
        return steps_taken

class PipeSegment:
    Ground = 0b0000
    N = 0b1000
    S = 0b0100
    E = 0b0010
    W = 0b0001
    Start = 0b1111
    _cache = {}
    _valid_shapes = set(i | j for i, j in combinations([N, S, E, W, Start], 2))

    @classmethod
    def get_shape(cls, shape):
        if isinstance(shape, int):
            if shape not in _valid_shapes:
                raise ValueError("Invalid shape integer")
            return int(shape)
        elif isinstance(shape, str):
            try:
                return {"|": cls.N | cls.S, "-": cls.E | cls.W, "L": cls.N | cls.E, "J": cls.N | cls.W,
                          "7": cls.S | cls.W, "F": cls.S | cls.E, ".": cls.Ground, "S": cls.Start}[shape]
            except KeyError:
                raise ValueError("Unrecognized pipe!")
        else:
            raise TypeError("Invalid input type, expected string or integer")

    @classmethod
    def dir_to_rel_coords(cls, direction):
        return {cls.N: (0, -1), cls.S: (0, 1), cls.E: (1, 0), cls.W: (-1, 0)}[direction]

    @classmethod
    def invert_direction(cls, direction):
        return {cls.N: cls.S, cls.S: cls.N, cls.E: cls.W, cls.W: cls.E}[direction]

    def can_go(self, direction):
        if direction not in (self.N, self.S, self.E, self.W):
            raise ValueError("Invalid direction, choose N, S, E, or W constants from class")
        return bool(self.shape & direction)

    def where_next(self, from_direction):
        if from_direction not in (self.N, self.S, self.E, self.W):
            raise ValueError("Invalid direction, choose N, S, E, or W constants from class")
        direction = self.shape & ~from_direction
        if direction == 0:
            raise ValueError("You can't have come from this direction")
        return direction

    def __new__(cls, s):
        shape = cls.get_shape(s)
        try:
            return cls._cache[shape]
        except KeyError:
            obj = super().__new__(cls)
            cls._cache[shape] = obj
            return obj

    def __init__(self, s):
        if not hasattr(self, "shape"):
            self.shape = type(self).get_shape(s)

    def __hash__(self):
        return self.shape

    def __str__(self):
        return {self.N | self.S: "\u2503", self.E | self.W: "\u2501", self.N | self.E:  "\u2517",  self.N | self.W: "\u251b",
                self.S | self.W: "\u2513", self.S | self.E: "\u250f", self.Ground: ".", self.Start: "*"}[self.shape]

    def __repr__(self):
        return type(self).__name__ + "(\"" + {self.N | self.S: "|", self.E | self.W: "-", self.N | self.E:  "L",  self.N | self.W: "J",
                self.S | self.W: "7", self.S | self.E: "F", self.Ground: ".", self.Start: "S"}[self.shape] + "\")"

def solve_pt1(inputfile):
    m = Maze(inputfile)
    print(f"The maze starts at {m.start}")
    steps_taken = m.walk_around()
    colored = False
    for y, line in enumerate(str(m).splitlines()):
        printline = ""
        for x, char in enumerate(line):
            if not colored and (x,y) in steps_taken:
                printline += "\x1b[33m"
                colored = True
            elif colored and (x,y) not in steps_taken:
                printline += "\x1b[0m"
                colored = False
            printline += char
        print(printline)

    print(f"It looks like {len(steps_taken) // 2} steps to the furthest point in the route")


def solve_pt2(inputfile):
    print("Not implemented yet")

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
