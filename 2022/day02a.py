#!/usr/bin/env python3

class Handshape:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    def __init__(self, token):
        if token.lower() in ('a', 'x'):
            self.shape = self.ROCK
        elif token.lower() in ('b', 'y'):
            self.shape = self.PAPER
        elif token.lower() in ('c', 'z'):
            self.shape = self.SCISSORS
        else:
            raise ValueError("I don't know who you think you are or what you hope to accomplish here, but I haven't got time for it")
    def __repr__(self):
        if self.shape == self.ROCK:
            return "Rock"
        elif self.shape == self.PAPER:
            return "Paper"
        elif self.shape == self.SCISSORS:
            return "Scissors"
    def __gt__(self, other):
        return (self.shape == other.shape + 1) or (self.shape == self.ROCK and other.shape == other.SCISSORS)
    def __eq__(self, other):
        return self.shape == other.shape
    def value(self):
        return self.shape

def fight(opponent, me):
    points = me.value()
    if me == opponent:
        points += 3
    elif me > opponent:
        points += 6
    return points

if __name__ == "__main__":
    with open("day02.txt", "r") as f:
        data = f.read().splitlines()
    points = 0
    for line in data:
        opponent, me = map(lambda x: Handshape(x), line.split())
        points += fight(opponent, me)
    print(f"You've ended up with {points} points")
