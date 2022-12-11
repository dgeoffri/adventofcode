#!/usr/bin/env python3

class Rope:
    directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

    def __init__(self):
        self.head = [0, 0]
        self.tail = self.head.copy()

    def _tail_must_move(self):
        return (abs(self.head[0] - self.tail[0]) > 1) or (abs(self.head[1] - self.tail[1]) > 1)

    def move(self, direction):
        cmp = lambda a, b: (a > b) - (a < b)
        x, y = Rope.directions[str(direction).upper()]
        self.head[0] += x
        self.head[1] += y
        if self._tail_must_move():
            for i in (0, 1):
                self.tail[i] += cmp(self.head[i], self.tail[i])
        return self

    def __repr__(self):
        return (f"Head: {self.head}, tail: {self.tail}")


def find_tail_visitation_spot_count(moves):
    r = Rope()
    tail_visitations = set()
    for move in moves:
        print(move)
        for _ in range(int(move[1])):
            r.move(move[0])
            tail_visitations.add(tuple(r.tail))
            print(r)
    return len(tail_visitations)


if __name__ == "__main__":
    # from io import StringIO
    # with StringIO("""R 4
    # U 4
    # L 3
    # D 1
    # R 4
    # D 1
    # L 5
    # R 2""") as f:
    with open("day09.txt", "r") as f:
        moves = [tuple(line.split(" ")) for line in f.read().splitlines()]
    count = find_tail_visitation_spot_count(moves)
    print(f"Tail visited {count} locations at least once.")
