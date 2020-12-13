#!/usr/bin/env python
import itertools

if __name__ == "__main__":
    with open('day10.txt', 'r') as f:
        inputdata = map(int, f.read().splitlines())
    inputdata.append(max(inputdata) + 3)
    start = 0
    max = inputdata[-1]
    chains = [[start]]
    did_something = True
    running_count = 0
    while did_something:
        did_something = False
        for chain in chains:
            choices = []
            for i in range(1, 4):
                if (chain[-1] + i) in inputdata:
                    choices.append(chain[-1] + i)
            if len(choices):
                for choice in choices[1:]:
                    chains.append([i for i in chain] + [choice])
                chain.append(choices[0])
                did_something = True
            else:
                if chain[-1] != max:
                    running_count += 1
                chains.remove(chain)
                did_something = True
            # print chains
    # successful_chains = filter(lambda x: x[-1] == max, chains)
    print "{} chains in progress, {} viable chains found so far".format(len(chains), running_count)
