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
    def count(self):
        return sum(row.count("#") for row in self.seatdata)
    def __str__(self):
        return '\n'.join(self.seatdata)

if __name__ == "__main__":
    with open('day11.txt', 'r') as f:
        seats = seat_arrangement(f.read().splitlines())
    while(seats.iterate()):
        # print seats
        pass
    print seats
    print "At the end, {} seats are occupied".format(seats.count())