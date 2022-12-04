#!/usr/bin/env python3

PRIORITIES = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_next_3(longlist):
    while len(longlist):
        yield [longlist.pop(0) for x in (0,1,2)]

def find_common_item_type(group_of_3_rucksacks):
    if len(group_of_3_rucksacks) != 3:
        raise ValueError("You need to pass in a group of 3 rucksacks otherwise I can't help you")
    rucksacks_as_deduped_list = list(map(set, group_of_3_rucksacks))
    rucksacks_as_deduped_list.sort(key=len)
    for check in rucksacks_as_deduped_list[0]:
        if check in rucksacks_as_deduped_list[1] and check in rucksacks_as_deduped_list[2]:
            return check
    else:
        raise ValueError("These elves have not an item in common!")

def outgrabe(first, second):
    for i in first:
        if i in second:
            return PRIORITIES.index(i)

if __name__ == "__main__":
    with open("day03.txt", "r") as fp:
        data = fp.read().splitlines()
    priorities = []
    for baggroup in get_next_3(data):
        priorities.append(PRIORITIES.index(find_common_item_type(baggroup)))
    print(f"Sum of the priorities of the items in each elvengroup is {sum(priorities)}")
