#!/usr/bin/env python3

lookup = {'<': '>', '(': ')', '[': ']', '{': '}'}
points = {')':3, ']': 57, '}': 1197, '>': 25137}

class ValidationError(Exception):
    def __init__(self, expected, found):
        self.expected = expected
        self.found = found

def validate_line(line):
    stack = []
    for char in line:
        if char in lookup.keys():
            stack.append(char)
        elif char in lookup.values():
            expected = lookup[stack.pop()]
            if char != expected:
                raise ValidationError(expected, char)
    return True

if __name__ == "__main__":
    with open("day10.txt", "r") as inputfile:
        inputlines = inputfile.read().splitlines()
    score = 0
    for line in inputlines:
        try:
            if validate_line(line):
                print("Line is valid: {}".format(line))
        except ValidationError as e:
            print("Line is corrupted -- expected {}, found {}:  {}".format(e.expected, e.found, line))
            score += points[e.found]
    print("Input was highly corrupted, for a total score of {} points".format(score))
