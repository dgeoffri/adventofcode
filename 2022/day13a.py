#!/usr/bin/env python3

import json


def are_lists_ordered(left, right):
    for i, a in enumerate(left):
        try:
            b = right[i]
        except IndexError:
            print("Right side ran out of items -- False")
            return False
        if type(a) == int and type(b) == int:
            print(f"Comparing {a}  and {b}")
            if a < b:
                print("True")
                return True
            if a > b:
                print("False")
                return False
        else:
            if type(a) == int:
                a = [a]
            if type(b) == int:
                b = [b]
            inner_ordered = are_lists_ordered(a, b)
            if inner_ordered != None:
                return inner_ordered
    if len(right) > len(left):
        print("Left side ran out of items -- True")
        return True
    return None


def check_pair(pair: str):
    left, right = map(json.loads, pair.splitlines())
    return are_lists_ordered(left, right)


if __name__ == "__main__":
    # from io import StringIO

    # puzzle_input = StringIO(
    #     "[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]\n")
    puzzle_input = open("day13.txt", "r")
    with puzzle_input as f:
        pairs = f.read().split("\n\n")
    correctly_ordered_pairs = [i + 1 for i, pair in enumerate(pairs) if check_pair(pair) in (True, None)]
    print(f"Correctly ordered pairs are pairs {correctly_ordered_pairs}, for a sum of {sum(correctly_ordered_pairs)}")
