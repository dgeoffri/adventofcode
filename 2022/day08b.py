#!/usr/bin/env python3

from functools import reduce
import operator


def find_highest_scenic_scores(data):
    NUM_ROWS = len(data)
    NUM_COLS = len(data[0])
    height_scores = [[0] * NUM_COLS for _ in range(0, NUM_ROWS)]

    for y_to_check in range(1, NUM_ROWS):
        for x_to_check in range(1, NUM_COLS):
            visible_trees = [0, 0, 0, 0]
            # Check towards the left
            for scan_x in range(x_to_check - 1, -1, -1):
                visible_trees[0] += 1
                if data[y_to_check][scan_x] >= data[y_to_check][x_to_check]:
                    break
            # Check towards top
            for scan_y in range(y_to_check - 1, -1, -1):
                visible_trees[1] += 1
                if data[scan_y][x_to_check] >= data[y_to_check][x_to_check]:
                    break
            # Check towards right
            for scan_x in range(x_to_check + 1, NUM_COLS):
                visible_trees[2] += 1
                if data[y_to_check][scan_x] >= data[y_to_check][x_to_check]:
                    break
            # Check towards bottom
            for scan_y in range(y_to_check + 1, NUM_ROWS):
                visible_trees[3] += 1
                if data[scan_y][x_to_check] >= data[y_to_check][x_to_check]:
                    break
            height_scores[y_to_check][x_to_check] = reduce(operator.mul, visible_trees)
    return max([col for row in height_scores for col in row])


if __name__ == "__main__":
    with open("day08.txt", "r") as f:
        data = [list(line) for line in f.read().splitlines()]
    print(f"The tree with the highest scenic score has a scenic score of: {find_highest_scenic_scores(data)}")
