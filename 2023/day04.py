#!/usr/bin/env python3

import sys
from collections import namedtuple

DAY = 4
USE_SAMPLE_DATA = False
SAMPLE_DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def readcards(inputfile):
    cards = []
    Picks = namedtuple("Picks", "winning mine")
    for line in inputfile:
        _, line = line.strip().split(": ", maxsplit=1)
        winning_numbers, my_numbers = line.split(" | ", maxsplit=1)
        winning_numbers = list(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        cards.append(Picks(winning_numbers, my_numbers))
    return cards


def solve_pt1(inputfile):
    cards = readcards(inputfile)
    total_score = 0
    for card in cards:
        winning_number_count = len([number for number in card.mine if number in card.winning])
        card_value = 0 if winning_number_count == 0 else 2 ** (winning_number_count - 1)
        # print(F"Card i has {winning_number_count} winning numbers for a value of {card_value}")
        total_score += card_value
    print(f"Total score: {total_score}")


def solve_pt2(inputfile):
    cards = readcards(inputfile)
    cards = [{"card": card, "copies": 1} for card in cards]
    for cardnum, card in enumerate(cards):
        winning_number_count = len([number for number in card["card"].mine if number in card["card"].winning])
        for i in range(winning_number_count):
            cards[cardnum + 1 + i]["copies"] += card["copies"]
        print(F"Card {cardnum + 1} ({card['copies']} copies) has {winning_number_count} winning numbers")
    print(f"Total number of cards: {sum((card['copies'] for card in cards))}")


if __name__ == "__main__":
    if USE_SAMPLE_DATA:
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
