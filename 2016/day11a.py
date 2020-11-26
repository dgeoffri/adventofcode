#!/usr/bin/env python

import re, copy, itertools

class Item(object):
    def __init__(self, text):
        if text.endswith(" generator"):
            self.type = "g"
            self.element = text[:len(text) - len(" generator")]
        elif text.endswith("-compatible microchip"):
            self.type = "m"
            self.element = text[:len(text) - len("-compatible microchip")]
        else:
            raise Exception("Unknown object")
    def __str__(self):
        if self.type == "g":
            return "a %s generator" % self.element
        elif self.type == "m":
            return "a %s-compatible microchip" % self.element
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(self.type + self.element)

class Board(object):
    def __init__(self, floormap, floor):
        self.floormap = copy.deepcopy(floormap)
        self.floor = floor
    def __str__(self):
        retstr = "You are on floor %d\n" % (self.floor + 1)
        for x in xrange(len(self.floormap)):
            retstr += "Floor %d contains: %s\n" % (x + 1, str(self.floormap[x]))
        return retstr
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash((frozenset(x) for x in self.floormap))
    def findmoves(self):
        if self.floor == 0:
            print "You can only go up"
        elif self.floor == len(self.floormap):
            print "You can only go down"
        else:
            print "Who are you, and what have you done with sanity?"
        takeitems = self.floormap[self.floor]
        takeitems += itertools.combinations(self.floormap[self.floor], 2)
        print "You can take with you: %s" % takeitems

if __name__ == "__main__":
    inputdata = open("day11.txt").read().splitlines()
    r = re.compile("a ([^,.]+)")
    floormap = [ None, None, None, None ]
    for floor in xrange(4):
        floormap[floor] = [ Item(i) for i in r.findall(inputdata[floor]) ]
    board = Board(floormap, 0)

