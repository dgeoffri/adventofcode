#!/usr/bin/env python3

import sys

DAY = 1
SAMPLE_DATA = """3   4
4   3
2   5
1   3
3   9
3   3
"""

def solve_pt1(inputfile):
    list1 = []
    list2 = []
    for line in inputfile:
        a, b = map(int, line.strip().split())
        list1.append(a)
        list2.append(b)
    list1.sort()
    list2.sort()
    total_distance = 0
    assert len(list1) == len(list2)
    for i in range(len(list1)):
        distance = abs(list2[i] - list1[i])
        # print(f"{list2[i]} - {list1[i]} = {distance}")
        total_distance += distance
    print(f"The total distance between the lists is {total_distance}")


def solve_pt2(inputfile):
    list1 = []
    list2 = []
    for line in inputfile:
        a, b = map(int, line.strip().split())
        list1.append(a)
        list2.append(b)
    similarity_score = 0
    assert len(list1) == len(list2)
    for i in list1:
        occurrences = list2.count(i)
        score = i * occurrences
        # print(f"{i} occurs in list 2 {occurrences} times for a score of {score}")
        similarity_score += score
    print(f"The similarity score between the lists is {similarity_score}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-e":
        from io import StringIO
        puzzle_input = StringIO(SAMPLE_DATA)
    else:
        try:
            puzzle_input = open("day{:02d}.txt".format(DAY), "r")
        except OSError as e:
            print("Something went horribly wrong: {}".format(e))
            sys.exit(1)

    with puzzle_input as f:
        print("---PART 1---")
        solve_pt1(f)
        f.seek(0)
        print("\n---PART 2---")
        solve_pt2(f)
