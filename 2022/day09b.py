#!/usr/bin/env python3

class RopeSegment:
    def __init__(self):
        self.head = [0, 0]
        self.tail = self.head.copy()

    def _tail_must_move(self):
        return (abs(self.head[0] - self.tail[0]) > 1) or (abs(self.head[1] - self.tail[1]) > 1)

    def move(self, direction):
        x, y = direction
        cmp = lambda a, b: (a > b) - (a < b)
        self.head[0] += x
        self.head[1] += y
        tail_movement_vector = None
        if self._tail_must_move():
            tail_movement_vector = tuple(cmp(self.head[i], self.tail[i]) for i in (0, 1))
            for i in (0, 1):
                self.tail[i] += tail_movement_vector[i]
        return tail_movement_vector

    def __repr__(self):
        return (f"Head: {self.head}, tail: {self.tail}")


class Rope:
    directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

    def __init__(self, number_of_knots=10):
        self.rope = [RopeSegment() for _ in range(number_of_knots - 1)]

    def move(self, direction):
        for segment in self.rope:
            if direction:
                direction = segment.move(direction)
            else:
                continue
        return tuple(self.rope[-1].tail)


def find_tail_visitation_spot_count(moves):
    r = Rope(10)
    tail_visitations = set()
    for move in moves:
        for _ in range(int(move[1])):
            tail_position = r.move(Rope.directions[str(move[0]).upper()])
            tail_visitations.add(tail_position)
    return len(tail_visitations)


if __name__ == "__main__":
    #     from io import StringIO
    #     with StringIO("""R 5
    # U 8
    # L 8
    # D 3
    # R 17
    # D 10
    # L 25
    # U 20""") as f:
    with open("day09.txt", "r") as f:
        moves = [tuple(line.split(" ")) for line in f.read().splitlines()]
    count = find_tail_visitation_spot_count(moves)
    print(f"Tail visited {count} locations at least once.")