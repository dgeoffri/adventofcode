#!/usr/bin/env python

class seat_arrangement(object):
    def __init__(self, seatdata):
        self.seatdata = seatdata
        self.rows = len(seatdata)
        self.columns = min(map(len, seatdata))
    def iterate(self):
        new_seatdata = []
        for j in xrange(self.rows):
            new_seatdata.append("")
            for i in xrange(self.columns):
                occupied_neighbors = 0
                for y in xrange(max(0, j - 1), min(self.rows, j + 2)):
                    for x in xrange(max(0, i - 1), min(self.columns, i + 2)):
                        if (x, y) == (i, j):
                            # print "I refuse to check myself ({}, {} == {}, {})".format(x, y, i, j)
                            continue    # don't count yourself
                        else:
                            # print "Checking seat {}, {} (working on seat {}, {})".format(x, y, i, j)
                            if self.seatdata[y][x] == '#':
                                occupied_neighbors += 1
                new_seat = self.seatdata[j][i]
                if self.seatdata[j][i] == 'L':
                    if occupied_neighbors == 0:
                        new_seat = '#'
                elif self.seatdata[j][i] == '#':
                    if occupied_neighbors >= 4:
                        new_seat = 'L'
                new_seatdata[j] += new_seat
                # print "Occupied neighbors = {}, current seat = {}, new seat = {}".format(occupied_neighbors, self.seatdata[j][i], new_seat)
        changed = (self.seatdata != new_seatdata)
        self.seatdata = new_seatdata
        return changed
    def iterate_partb(self):
        new_seatdata = []
        for j in xrange(self.rows):
            new_seatdata.append("")
            for i in xrange(self.columns):
                occupied_seats_seen = 0
                for y in xrange(-1, 2):
                    for x in xrange(-1, 2):
                        if (x, y) == (0, 0):
                            # print "I refuse to check myself ({}, {} == {}, {})".format(x, y, i, j)
                            continue    # this wouldn't make sense
                        else:
                            my_x, my_y = i + x, j + y
                            seen_a_seat = False
                            while (0 <= my_x < self.columns) and (0 <= my_y < self.rows) and not seen_a_seat:
                                # print "Checking seat {}, {} (working on seat {}, {})".format(my_x, my_y, i, j)
                                if self.seatdata[my_y][my_x] == '#':
                                    occupied_seats_seen += 1
                                    seen_a_seat = True
                                elif self.seatdata[my_y][my_x] == 'L':
                                    seen_a_seat = True
                                my_x += x
                                my_y += y
                new_seat = self.seatdata[j][i]
                if self.seatdata[j][i] == 'L':
                    if occupied_seats_seen == 0:
                        new_seat = '#'
                elif self.seatdata[j][i] == '#':
                    if occupied_seats_seen >= 5:
                        new_seat = 'L'
                new_seatdata[j] += new_seat
                # print "Occupied neighbors = {}, current seat = {}, new seat = {}".format(occupied_neighbors, self.seatdata[j][i], new_seat)
        changed = (self.seatdata != new_seatdata)
        self.seatdata = new_seatdata
        return changed
    def count(self):
        return sum(row.count("#") for row in self.seatdata)
    def __str__(self):
        return '\n'.join(self.seatdata)

if __name__ == "__main__":
    with open('day11.txt', 'r') as f:
        seats = seat_arrangement(f.read().splitlines())
    while(seats.iterate_partb()):
        # print seats
        pass
    print seats
    print "At the end, {} seats are occupied".format(seats.count())