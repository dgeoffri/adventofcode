#!/usr/bin/env python

if __name__ == "__main__":
    with open('day13.txt', 'r') as f:
        f.readline()
        buses = [(int(y), x) for x, y in enumerate(f.readline().split(",")) if y.isdigit()]
    buses = [(int(y), x) for x, y in enumerate("67,7,x,59,61".split(",")) if y.isdigit()]
    print buses
    largest_id, slot = max(buses)
    t = largest_id - slot
    print largest_id, t
    all_buses_departed = False
    while not all_buses_departed:
        departures = []
        for bus_id, slot in buses:
            departures.append((t + slot) % bus_id == 0)
        # print departures
        all_buses_departed = all(departures)
        if all_buses_departed:
            print "All departed on time when t was {}!".format(t)
        # print t
        t += largest_id
