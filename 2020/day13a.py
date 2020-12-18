#!/usr/bin/env python

if __name__ == "__main__":
    with open('day13.txt', 'r') as f:
        depart_time = int(f.readline())
        bus_ids = map(int, filter(lambda x: x.isdigit(), f.readline().split(",")))
        wait_times = {}
        for i in bus_ids:
            # print "{} - ({} % {}) is {}".format(i, depart_time, i, i - (depart_time % i))
            wait_times[i - (depart_time % i)] = i
        shortest_wait_time = min(wait_times.keys())
        print "Shortest wait time is {} minutes, for bus ID {}.  The product of those 2 numbers is {}".format(
            shortest_wait_time, wait_times[shortest_wait_time], shortest_wait_time * wait_times[shortest_wait_time])
