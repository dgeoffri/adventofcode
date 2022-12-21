#!/usr/bin/env python3

import json
from functools import cmp_to_key


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


def sort_cmp(a, b):
    cmp_dict = {False: -1, None: 0, True: 1}
    return cmp_dict[are_lists_ordered(a, b)]


def import_json(inputdata: list):
    return list(map(json.loads, inputdata))


if __name__ == "__main__":
    # from io import StringIO

    # puzzle_input = StringIO(
    #    "[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]\n")
    puzzle_input = open("day13.txt", "r")
    with puzzle_input as f:
        pairs = import_json([pair for pair in f.read().splitlines() if len(pair)])
    divider_packets = [[[2]], [[6]]]
    pairs += divider_packets
    sorted_pairs = sorted(pairs, key=cmp_to_key(sort_cmp), reverse=True)
    divider_indices = tuple(sorted_pairs.index(divider) + 1 for divider in divider_packets)
    print(f"Divider packets located at slots {divider_indices[0]} and {divider_indices[1]}")
    print(f"Decoder key: {divider_indices[0] * divider_indices[1]}")
