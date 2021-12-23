#!/usr/bin/env python3

def create_lookup(all_digits):
    def find_and_remove_by_count(count):
        segments = next(filter(lambda x: len(x) == count, all_digits))
        all_digits.remove(segments)
        return segments
    digit_lookup = {}    # create dict from digits to set of lit segments
    # find '1'
    digit_lookup[1] = find_and_remove_by_count(2)
    # find '7'
    digit_lookup[7] = find_and_remove_by_count(3)
    # find '4'
    digit_lookup[4] = find_and_remove_by_count(4)
    # find '8'
    digit_lookup[8] = find_and_remove_by_count(7)
    # find '9'
    subselection = list(filter(lambda x: len(x) == 6, all_digits))
    segments = next(filter(lambda x: digit_lookup[4].issubset(x), subselection))
    all_digits.remove(segments)  # out of the pool, buddy
    digit_lookup[9] = segments
    # note lower-left-hand segment
    lower_left = digit_lookup[8] - digit_lookup[9]  # only one segment is missing from 9, 8 has all lit
    # find '2'
    subselection = list(filter(lambda x: len(x) == 5, all_digits))
    segments = next(filter(lambda x: lower_left.issubset(x), subselection))
    subselection.remove(segments) # and you
    all_digits.remove(segments)   # not there either
    digit_lookup[2] = segments
    # note upper-right-hand segment
    upper_right = segments & digit_lookup[1]
    # find '3'
    segments = next(filter(lambda x: upper_right.issubset(x), subselection))
    subselection.remove(segments) # bye, felicia
    all_digits.remove(segments)   # not there either
    digit_lookup[3] = segments
    # find '5'
    segments = subselection.pop() # last one in the kiddie pool
    all_digits.remove(segments)
    digit_lookup[5] = segments
    # find '6'
    subselection = list(filter(lambda x: len(x) == 6, all_digits))
    segments = next(filter(lambda x: not upper_right.issubset(x), subselection))
    subselection.remove(segments) # 6 is OUT
    all_digits.remove(segments)   # all the way out
    digit_lookup[6] = segments
    # find '0'
    segments = subselection.pop() # last 6-grouping
    all_digits.remove(segments)
    digit_lookup[0] = segments

    # return invert list for lookup table
    return dict(map(reversed, digit_lookup.items()))

if __name__ == "__main__":
    with open("day08.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()
    rightsides = [ line.split("|")[1].split() for line in lines ]
    lit_segment_counts = [ list(map(len, display)) for display in rightsides ]
    count = len(list(filter(lambda x: x in map(int, "2347"), sum(lit_segment_counts, []))))
    print("The digit 1, 4, 7, or 8 occurs {} times.".format(count))

    total = 0
    for line in lines:
        leftside, rightside = list(map(lambda x: list(map(frozenset,x.split())), line.split('|')))
        table = create_lookup(leftside)
        digits = [ table[digit] for digit in rightside ]
        number = int(''.join(map(str,digits)))
        total += number
        print("Display reads: {}".format(number))
    print("Sum of all the numbers displayed is {}".format(total))
