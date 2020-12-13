#!/usr/bin/env python
# coding=utf-8

class Ship(object):
    DIRECTIONS = 'ESWN'

    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint = [10, -1]

    def rotate_waypoint(self, turn_direction, degrees):
        turn_direction = turn_direction[0].upper()
        if degrees % 90:
            print "I only know how to rotate the waypoint in 90° increments -- doing floor division"
        turns = (degrees // 90) % 4
        if turns == 0:
            print "A complete rotation is no rotation at all!"
        else:
            if turn_direction == "L":
                turns = 4 - turns
            for _ in xrange(turns):
                self.waypoint[0], self.waypoint[1] = -self.waypoint[1], self.waypoint[0]
        print "Waypoint rotated {} {} degrees and is now located at {}".format(turn_direction, degrees,
                                                                               self.get_waypoint_location())

    def move_waypoint(self, move_direction, distance):
        direction_vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
        move_direction = move_direction[0].upper()
        if move_direction in self.DIRECTIONS:
            xvec, yvec = direction_vectors[self.DIRECTIONS.index(move_direction)]
        else:
            raise ValueError("Direction must be one of N, S, E, W")
        self.waypoint[0] += distance * xvec
        self.waypoint[1] += distance * yvec
        print "Waypoint moved {} {} units and is now located at {}".format(move_direction, distance,
                                                                           self.get_waypoint_location())

    def move_ship(self, magnitude):
        self.x += self.waypoint[0] * magnitude
        self.y += self.waypoint[1] * magnitude
        print "Ship moved to waypoint {} times and is now located at {}".format(magnitude, self.get_ship_location())

    def execute_command(self, (command, magnitude)):
        if command[0].upper() in "NSEW":
            self.move_waypoint(command, magnitude)
        elif command[0].upper() in "LR":
            self.rotate_waypoint(command, magnitude)
        elif command[0].upper() == 'F':
            self.move_ship(magnitude)
        else:
            raise ValueError("Command \"{}\" not understood".format(command))

    def get_ship_location(self):
        return (self.x, self.y)

    def get_waypoint_location(self):
        return (self.waypoint[0], self.waypoint[1])

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    with open('day12.txt', 'r') as f:
        inputdata = map(lambda line: (line[:1], int(line[1:])), f.read().splitlines())
    ship = Ship()
    for instruction in inputdata:
        ship.execute_command(instruction)
    print "Ship has a Manhattan distance of {} from its point of origin".format(ship.get_manhattan_distance())
