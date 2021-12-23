#!/usr/bin/env python3

class Fish(object):
    def __init__(self, timer):
        self.timer = timer
    def __repr__(self):
        return str(self.timer)
    def age(self):
        if self.timer == 0:
            self.timer = 6
            return Fish(8)
        else:
            self.timer -= 1
            return None

if __name__ == "__main__":
    with open("day06.txt", "r") as inputfile:
        fishes = [Fish(i) for i in map(int, inputfile.read().strip().split(','))]
    print(fishes)
    for days in range(80):
        newfishes = []
        for fish in fishes:
            newfishes.append(fish.age())
        fishes += filter(lambda x: x, newfishes)
    print("After {} days there are {} fishes.".format(80, len(fishes)))
