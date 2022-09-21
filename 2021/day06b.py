#!/usr/bin/env python3

class FishAges(object):
    def __init__(self, loadfishes=[]):
        self.slots = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        for fish in loadfishes:
            assert fish >= 0 and fish <= 6
            self.slots[fish] += 1
    def age(self, days = 1):
        for _ in range(days):
            temp = self.slots.pop(0)
            self.slots[6] += temp
            self.slots.append(temp)
    def count(self):
        return sum(self.slots)

if __name__ == "__main__":
    with open("day06.txt", "r") as inputfile:
        fish_ages = FishAges(map(int, inputfile.read().strip().split(',')))
    fish_ages.age(80)
    print("After {} days there are {} fishes.".format(80, fish_ages.count()))
    fish_ages.age(256 - 80)
    print("After {} days there are {} fishes.".format(256, fish_ages.count()))
