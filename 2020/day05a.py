#!/usr/bin/env python

if __name__ == "__main__":
    with open('day05.txt', 'r') as f:
        inputdata = f.read().splitlines()

    seat_ids = []
    for seat in inputdata:
        seat_y = seat[:7]
        seat_x = seat[7:]
        y_min = 0
        y_max = 127
        x_min = 0
        x_max = 7
        for c in seat_y:
            if c=='F':
                y_max -= (1 + y_max - y_min) / 2
            elif c=='B':
                y_min += (1 + y_max - y_min) / 2
            else:
                print "Coding error"
        if y_min != y_max:
            print "Error, y_min != y_max"
        for c in seat_x:
            if c=='L':
                x_max -= (1 + x_max - x_min) / 2
            elif c=='R':
                x_min += (1 + x_max - x_min) / 2
            else:
                print "Coding error"
        if x_min != x_max:
            print "Error, x_min != x_max"
        seat_id = y_min * 8 + x_min
        # print "Seat is in row {}, column {}.  Seat ID is {}.".format(y_min, x_min, seat_id)
        seat_ids.append(seat_id)
    print "Highest seat ID is {}".format(max(seat_ids))




