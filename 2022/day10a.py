#!/usr/bin/env python3

from queue import Queue


class CPU:
    def __init__(self, inputqueue):
        self.X = 1
        self.queue = inputqueue

    def cycle_accurate_X(self):
        q = self.queue
        while not q.empty():
            instruction = q.get()
            if len(instruction) == 1:
                assert instruction[0] == "noop"
                yield self.X
            elif len(instruction) == 2:
                assert instruction[0] == "addx"
                yield self.X
                yield self.X
                self.X += int(instruction[1])


def find_sum_of_values_at_positions(generator, list_of_positions):
    get_it_all = list(generator)
    values_at_positions = [get_it_all[position - 1] * position for position in list_of_positions]
    print(values_at_positions)
    return sum(values_at_positions)


if __name__ == "__main__":
    # from io import StringIO
    # puzzle_input = StringIO("addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop\n")
    puzzle_input = open("day10.txt", "r")
    with puzzle_input as f:
        instructions = [tuple(line.split(" ")) for line in f.read().splitlines()]

    CPU_cacheline = Queue()
    for instruction in instructions:
        CPU_cacheline.put(instruction)

    cpu = CPU(CPU_cacheline)
    answer = find_sum_of_values_at_positions(cpu.cycle_accurate_X(), [20, 60, 100, 140, 180, 220])

    print(f"The answer is {answer}")
