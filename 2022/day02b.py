#!/usr/bin/env python3

class Handshape:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    def __init__(self, token):
        if type(token) == int and token >= 1 and token <= 3:
            self.shape = token
        elif token.lower() == 'a':
            self.shape = self.ROCK
        elif token.lower() == 'b':
            self.shape = self.PAPER
        elif token.lower() == 'c':
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
    def shape_that_ties(self):
        return Handshape(self.shape)
    def shape_that_defeats(self):
        shape = self.shape + 1
        if shape > 3:
            shape -= 3
        return Handshape(shape)
    def shape_that_gets_defeated(self):
        shape = self.shape - 1
        if shape < 1:
            shape += 3
        return Handshape(shape)

def fight(opponent, me):
    points = me.value()
    if me == opponent:
        points += 3
    elif me > opponent:
        points += 6
    return points

def choose_move(opponent, legend):
    if legend.lower() == 'x':
        return opponent.shape_that_gets_defeated()
    elif legend.lower() == 'y':
        return opponent.shape_that_ties()
    elif legend.lower() == 'z':
        return opponent.shape_that_defeats()
    else:
        raise ValueError("I don't know who you think you are or what you hope to accomplish here, but I haven't got time for it")

if __name__ == "__main__":
    with open("day02.txt", "r") as f:
        data = f.read().splitlines()
    points = 0
    for line in data:
        opponent, me = line.split()
        opponent = Handshape(opponent)
        me = choose_move(opponent, me)
        points += fight(opponent, me)
    print(f"You've ended up with {points} points")
