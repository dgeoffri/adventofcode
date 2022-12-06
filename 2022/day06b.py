#!/usr/bin/env python3

def notUnique(buffer):
    assert len(buffer) == 14, "Without being given a 4 byte string, I can't help you"
    found = ""
    for i in buffer:
        if i in found:
            return True
        found += i
    return False

def find_start(data):
    endbyte = 14
    buffer = data[endbyte - 14:endbyte]
    while notUnique(buffer):
        endbyte += 1
        buffer = data[endbyte - 14:endbyte]
    return endbyte

if __name__ == "__main__":
    with open("day06.txt", "r") as f:
        data = f.read().strip()
    start = find_start(data)
    print(f"The first start packet occurs after reading byte {start}.")
