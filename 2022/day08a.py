#!/usr/bin/env python3

def count_visible_trees(data):
    NUM_ROWS = len(data)
    NUM_COLS = len(data[0])
    visible_map = []
    visible_map.append([True] * NUM_COLS)
    for _ in range(1, NUM_ROWS - 1):
        visible_map.append([True] + [False] * (NUM_COLS - 2) + [True])
    visible_map.append([True] * NUM_COLS)

    for y_to_check in range(1, NUM_ROWS):
        for x_to_check in range(1, NUM_COLS):
            # Check visibility from left
            for scan_x in range(0, x_to_check):
                if data[y_to_check][scan_x] >= data[y_to_check][x_to_check]:
                    break
            else:
                visible_map[y_to_check][x_to_check] = True
                continue
            # Check visibility from top
            for scan_y in range(0, y_to_check):
                if data[scan_y][x_to_check] >= data[y_to_check][x_to_check]:
                    break
            else:
                visible_map[y_to_check][x_to_check] = True
                continue
            # Check visibility from right
            for scan_x in range(NUM_COLS - 1, x_to_check, -1):
                if data[y_to_check][scan_x] >= data[y_to_check][x_to_check]:
                    break
            else:
                visible_map[y_to_check][x_to_check] = True
                continue
            # Check visibility from bottom
            for scan_y in range(NUM_ROWS - 1, y_to_check, -1):
                if data[scan_y][x_to_check] >= data[y_to_check][x_to_check]:
                    break
            else:
                visible_map[y_to_check][x_to_check] = True
                continue

    # Time 2 tally
    return sum([1 if column else 0 for row in visible_map for column in row])


if __name__ == "__main__":
    with open("day08.txt", "r") as f:
        data = [list(line) for line in f.read().splitlines()]
    print(f"Number of trees visible: {count_visible_trees(data)}")
