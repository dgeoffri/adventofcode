#!/usr/bin/env python
# coding=utf-8

class Ship(object):
    DIRECTIONS = 'ESWN'

    def __init__(self):
        self.facing_direction = 0
        self.x = 0
        self.y = 0

    def turn(self, turn_direction, degrees):
        plusorminus = {'R': 1, 'L': -1}
        turn_direction = turn_direction[0].upper()
        if degrees % 90:
            print "I only know how to turn in 90° increments -- doing floor division"
        try:
            self.facing_direction = (self.facing_direction + plusorminus[turn_direction] * (degrees // 90)) % 4
        except KeyError:
            raise ValueError("I only know how to turn left or right!")
        print "Ship is now facing {}".format(self.get_direction())

    def move(self, move_direction, distance):
        direction_vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
        move_direction = move_direction[0].upper()
        if move_direction == "F":
            xvec, yvec = direction_vectors[self.facing_direction]
        elif move_direction in self.DIRECTIONS:
            xvec, yvec = direction_vectors[self.DIRECTIONS.index(move_direction)]
        else:
            raise ValueError("Direction must be one of N, S, E, W, or F")
        self.x += distance * xvec
        self.y += distance * yvec
        print self.get_location()

    def execute_command(self, command, magnitude):
        if command[0].upper() in "NSEWF":
            self.move(command, magnitude)
        elif command[0].upper() in "LR":
            self.turn(command, magnitude)
        else:
            raise ValueError("Command \"{}\" not understood".format(command))

    def get_location(self):
        return "Ship is located at ({},{})".format(self.x, self.y)

    def get_direction(self):
        longname_directions = {"N": "north", "E": "east", "W": "west", "S": "south"}
        return longname_directions[self.DIRECTIONS[self.facing_direction]]

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    with open('day12.txt', 'r') as f:
        inputdata = map(lambda line: (line[:1], int(line[1:])), f.read().splitlines())
    ship = Ship()
    for instruction in inputdata:
        ship.execute_command(*instruction)
    print "Ship has a Manhattan distance of {} from its point of origin".format(ship.get_manhattan_distance())
