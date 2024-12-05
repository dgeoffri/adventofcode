#!/usr/bin/env python3

import sys
from collections import defaultdict

DAY = 5
SAMPLE_DATA = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def solve_pt1(inputfile):
    prerequisites = defaultdict(list)
    updates_list = []
    middle_page_number_sum = 0
    for line in inputfile:
        line = line.strip()
        if "|" in line:
            before, after = map(int, line.split("|"))
            prerequisites[after].append(before)
        elif "," in line:
            pagelist = list(map(int, line.split(",")))
            updates_list.append(pagelist)
        else:
            if len(line):
                print("Bad line!")
    for instruction_set in updates_list:
        in_order = True
        pages_printed = []
        for page in instruction_set:
            if page not in prerequisites:
                pages_printed.append(page)
            else:
                for prerequisite in prerequisites[page]:
                    if (prerequisite not in instruction_set):
                        pages_printed.append(page)
                        continue
                    elif (prerequisite not in pages_printed):
                        in_order = False
                        break
                if not in_order:
                    break
            if not in_order:
                break
        if not in_order:
            print(f"Printing instructions not in order: {', '.join(map(str, instruction_set))}")
        else:
            print(f"Printing instructions are in order: {', '.join(map(str, instruction_set))}")
            middle_page_number = instruction_set[(len(instruction_set)-1) // 2]
            middle_page_number_sum += middle_page_number
    print(f"Sum of middle page numbers of all printed pages: {middle_page_number_sum}")



def solve_pt2(inputfile):
    print("Not implemented yet")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-e":
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
