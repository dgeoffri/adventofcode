#!/usr/bin/env python3


import queue


class Map:
    def __init__(self, data: list):
        self.start_pos = None
        self.end_pos = None
        self.map = []
        for y, line in enumerate(data):
            mapline = list(map(lambda x: ord(x) - ord("a"), line))
            if not self.start_pos:
                for x, pos in enumerate(mapline):
                    if pos == -14:
                        self.start_pos = (x, y)
                        mapline[x] = 0
            if not self.end_pos:
                for x, pos in enumerate(mapline):
                    if pos == -28:
                        self.end_pos = (x, y)
                        mapline[x] = 25
            self.map.append(mapline)
        assert (self.start_pos is not None) and (self.end_pos is not None)


class Path:
    def __init__(self, coord: tuple, visited: list):
        self.x, self.y = coord
        self.visited = visited


def find_shortest_path(m: Map):
    start = m.end_pos
    visited = set()
    trailqueue = queue.Queue()
    trailqueue.put(Path(start, []))
    while not trailqueue.empty():
        trail = trailqueue.get()
        if (trail.x, trail.y) in visited:
            continue
        visited.add((trail.x, trail.y))
        if m.map[trail.y][trail.x] == 0:
            trailqueue.queue.clear()
            return len(trail.visited)
        for x, y in ((trail.x - 1, trail.y), (trail.x, trail.y - 1), (trail.x + 1, trail.y), (trail.x, trail.y + 1)):
            if (x < 0) or (y < 0) or (x >= len(m.map[0])) or (y >= len(m.map)):
                continue
            if m.map[y][x] - m.map[trail.y][trail.x] >= -1:
                trailqueue.put(Path((x, y), trail.visited + [(trail.x, trail.y)]))


if __name__ == "__main__":
    # from io import StringIO

    # puzzle_input = StringIO("Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi")
    puzzle_input = open("day12.txt", "r")
    with puzzle_input as f:
        terrain = f.read().splitlines()
    m = Map(terrain)
    shortest_path = find_shortest_path(m)
    print(f"The shortest path contains {shortest_path} steps")
