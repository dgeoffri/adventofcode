#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day09.txt', 'r') as f:
        inputdata = map(int, f.read().splitlines())
    inputdata_copy = [i for i in inputdata]
    failed = False
    while not failed:
        if len(filter(lambda (x, y): x + y == inputdata_copy[25], itertools.combinations(inputdata_copy[:25], 2))) < 1:
            failing_number = inputdata_copy[25]
            failed = True
        else:
            inputdata_copy.pop(0)
    print "Number {} fails the check!".format(failing_number)

    # this is pure, putrid trash, but it's past 2am.  please, future self, make a non-trash version of this?
    for i in range(len(inputdata)):
        for j in range(i, len(inputdata)):
            localsum = sum(inputdata[i:j])
            if localsum == failing_number:
                print "Found contiguous set from pos {} to {}".format(i,j)
                print min(inputdata[i:j]) + max(inputdata[i:j])