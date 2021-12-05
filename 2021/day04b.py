#!/usr/bin/env python3

class Board(object):
    def __init__(self, squares):
        self.squares = squares
        self.positions = {}
        self.covered_positions = set()
        self.already_won = False
        self.num_rows = len(squares)
        if len(set(map(len, squares))) > 1:
            raise ValueError("Can't handle jagged board")
        self.num_cols = len(squares[0])
        for y in range(self.num_rows):
            for x in range (self.num_cols):
                self.positions[self.squares[y][x]] = (x, y)
    def check_bingo(self, number):
        if (not self.already_won) and (number in self.positions):
            self.covered_positions.add(self.positions[number])
            cols_only = [ x for (x,y) in self.covered_positions ]
            if self.num_cols in [ cols_only.count(i) for i in set(cols_only) ]:
                self.already_won = True
                return True
            rows_only = [ y for (x,y) in self.covered_positions ]
            if self.num_rows in [ rows_only.count(i) for i in set(rows_only) ]:
                self.already_won = True
                return True
        return False
    def get_unmarked_sum(self):
        squares = self.squares
        for col, row in self.covered_positions:
            squares[row][col] = 0
        return sum([sum(row) for row in squares])
    def __repr__(self):
        return '\n'.join([' '.join(map(str,row)) for row in self.squares])

def get_board(infile):
    squares = []
    nextline = infile.readline().strip()
    if not len(nextline):
        return None
    while len(nextline):
        squares.append([*map(int, nextline.split())])
        nextline = infile.readline().strip()
    return Board(squares)

def get_drawing(infile):
    numbers = map(int, infile.readline().strip().split(','))
    infile.readline()
    return numbers

if __name__ == "__main__":
    boards = []
    with open("day04.txt", "r") as inputfile:
        numbers = get_drawing(inputfile)
        board = get_board(inputfile)
        while board:
            boards.append(board)
            board = get_board(inputfile)
    last_winner = False
    for number in numbers:
        bingo_results = [ board.check_bingo(number) for board in boards ]
        if any(bingo_results):
            last_winner = (bingo_results.index(True), number)
    if (last_winner):
        winner, number = last_winner
        print("Board {} won last, when {} was called!".format(winner, number))
        print(boards[winner])
        print("Sum of unmarked squares: {}".format(boards[winner].get_unmarked_sum()))
        print("Puzzle answer (sum * number): {}".format(boards[winner].get_unmarked_sum() * number))
    else:
        print("No bingos! (This should probably not happen)")
