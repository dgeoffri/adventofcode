#!/usr/bin/env python3

from queue import Queue
from collections import namedtuple

Move = namedtuple('Move', ['count', 'src', 'dest'])


class Puzzle:
    def __init__(self, filename=None):
        if filename:
            self.load_puzzle(filename)

    def load_puzzle(self, filename):
        state_lines = []
        # read file
        with open(filename, "r") as f:
            while len(l := f.readline().rstrip()):
                state_lines.append(l)
            move_lines = f.read().splitlines()
        # find column offsets for stacks
        offsets_dict = {}
        for offset, number in enumerate(state_lines[-1]):
            if number.isnumeric():
                offsets_dict[int(number)] = offset
        # load stacks, bottom up
        stacks = {}
        for line in state_lines[-2::-1]:
            for stack, column in offsets_dict.items():
                try:
                    if (c := line[column]).isalpha():
                        try:
                            stacks[stack].append(c)
                        except KeyError:
                            stacks[stack] = [c]
                except IndexError:
                    continue
        self.stacks = stacks
        # load moves
        moves = Queue()
        for line in move_lines:
            move, count, _from, src, _to, dest = line.split()
            assert move == "move", "Corrupted instruction list"
            assert _from == "from", "Corrupted instruction list"
            assert _to == "to", "Corrupted instruction list"
            moves.put(Move(int(count), int(src), int(dest)))
        self.moves = moves

    def do_move(self):
        if self.moves.empty():
            raise StopIteration("No moves left in queue")
        move = self.moves.get()
        temp_stack = []
        for i in range(move.count):
            temp_stack.append(self.stacks[move.src].pop())
        for i in range(move.count):
            self.stacks[move.dest].append(temp_stack.pop())

    def do_all_moves(self):
        while not self.moves.empty():
            self.do_move()

    @property
    def message(self):
        return ''.join([self.stacks[i][-1] for i in sorted(self.stacks)])


if __name__ == "__main__":
    puzzle = Puzzle('day05.txt')
    puzzle.do_all_moves()
    print(f"Your secret message is: {puzzle.message}")
