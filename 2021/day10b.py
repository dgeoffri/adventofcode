#!/usr/bin/env python3

lookup = {'<': '>', '(': ')', '[': ']', '{': '}'}
points = {')':3, ']': 57, '}': 1197, '>': 25137}
autocomplete_points = {x[1]: x[0]+1 for x in enumerate(")]}>")}

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
    return ''.join(map(lambda match: lookup[match], reversed(stack)))

if __name__ == "__main__":
    with open("day10.txt", "r") as inputfile:
        inputlines = inputfile.read().splitlines()
    errored_score, autocomplete_scores = 0, []
    for line in inputlines:
        try:
            complete_string = validate_line(line)
            if len(complete_string) == 0:
                print("Line is valid: {}".format(line))
            else:
                print("Line is valid but incomplete: {}".format(line))
                print("Auto-completed line: {}".format(line + complete_string))
                temp_score = 0
                for char in complete_string:
                    temp_score = (temp_score * 5) + autocomplete_points[char]
                autocomplete_scores.append(temp_score)
        except ValidationError as e:
            print("Line is corrupted -- expected {}, found {}:  {}".format(e.expected, e.found, line))
            errored_score += points[e.found]
    print("Input was highly corrupted, error score was {} points".format(errored_score))
    print("Middle value of the sorted autocomplete scores is {} points".format(sorted(autocomplete_scores)[len(autocomplete_scores) // 2]))
