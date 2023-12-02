#!/usr/bin/env python3

if __name__ == "__main__":
    with open("day01.txt", "r") as f:
        data = f.read().splitlines()
    calories_per_elf = []
    running_total = 0
    for line in data:
        if not len(line):
            calories_per_elf.append(running_total)
            running_total = 0
        else:
            running_total += int(line)
    print(f"The elf with the most calories has {max(calories_per_elf)} calories.")
    print(f"The sum of the calories carried by the top 3 elves is {sum(sorted(calories_per_elf)[-3:])} calories.")

