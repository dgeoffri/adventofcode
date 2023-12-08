#!/usr/bin/env python3

import sys
from functools import total_ordering
from collections import Counter

DAY = 7
USE_SAMPLE_DATA = False
SAMPLE_DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

@total_ordering
class Card:
    _cardorder = "23456789TJQKA"
    def __init__(self, card):
            if card not in self.__class__._cardorder:
                raise ValueError("Invalid card type")
            self._card = card
    @property
    def value(self):
        return self.__class__._cardorder.index(self._card) + 2
    def __eq__(self, other):
            return self._card == other._card
    def __lt__(self, other):
            return self.value < other.value
    def __str__(self):
        return self._card
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return ord(self._card)

@total_ordering
class Hand():
    def __init__(self, hand, bid, j_is_joker=False):
        if not len(hand) == 5:
            raise ValueError("Wrong number of cards in hand (need 5)")
        if j_is_joker:
            Card._cardorder = "J23456789TQKA"
        self._hand = [ Card(card) for card in hand ]
        if not type(bid) == int:
            raise ValueErrr("Bid must be an integer")
        self._bid = bid
        self._j_is_joker = j_is_joker

    @property
    def _relstrength(self):
        hand_counter = Counter(self)
        jokers = 0
        if self._j_is_joker:
            jokers = hand_counter[Card("J")]
            del(hand_counter[Card("J")])
        c = sorted(hand_counter.values(), reverse=True)
        if jokers == 5 or c[0] + jokers == 5:
            return 6
        elif c[0] + jokers == 4:
            return 5
        elif c[0] + jokers == 3 and c[1] == 2:
            return 4
        elif c[0] + jokers == 3:
            return 3
        elif c[0] + jokers == 2 and c[1] == 2:
            return 2
        elif c[0] + jokers == 2:
            return 1
        else:
            return 0
    def __iter__(self):
        return iter(self._hand)
    def __repr__(self):
        return f"Hand({repr(self._hand)}, bid={self._bid})"
    def __str__(self):
        return f"{''.join(map(str, self._hand))} {self._bid}"
    def __eq__(self, other):
        return sorted(self._hand) == sorted(other._hand)
    def __lt__(self, other):
        a, b = self._relstrength, other._relstrength
        if a < b:
            return True
        if a > b:
            return False
        for i in range(len(self._hand)):
            a, b = self._hand[i].value, other._hand[i].value
            if a < b:
                return True
            if a > b:
                return False


def solve(inputfile, j_is_joker=False):
    hands = []
    for line in inputfile:
        hand, bid = line.strip().split()
        hand = Hand(hand, int(bid), j_is_joker)
        hands.append(hand)
    total = 0
    for rank, hand in enumerate(sorted(hands), 1):
        # print(rank, hand, hand._relstrength)
        total += rank * hand._bid
    print(f"Total score: {total}")

def solve_pt1(inputfile):
    solve(inputfile)

def solve_pt2(inputfile):
    solve(inputfile, j_is_joker=True)

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
