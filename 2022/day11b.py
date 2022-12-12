#!/usr/bin/env python3

import operator
from functools import reduce

class Monkey:
    def __init__(self, monkeystring):
        self.inspection_count = 0
        monkeydata = monkeystring.rstrip().split('\n')
        monkey_number = monkeydata.pop(0).split(':')[0].split()
        assert monkey_number[0] == "Monkey" and monkey_number[1].isnumeric()
        self.id = int(monkey_number[1])
        need_params = ['Starting items', 'Operation', 'Test', 'If true', 'If false']
        params = {}
        for line in monkeydata:
            line = line.strip().split(":")
            if line[0] in need_params:
                params[line[0]] = line[1]
            else:
                raise ValueError(f"Bad configuration value \"{line[0]}: {line[1]}\" -- can't continue")
        if len(params) != len(need_params):
            raise ValueError(f"Error in input -- not all required parameters were specified")
        self.items = [int(x.strip()) for x in params['Starting items'].strip().split(",")]
        operation = params['Operation'].strip().split()
        assert ' '.join(operation[0:3]) == "new = old"
        assert operation[3] in "+*"
        # assert operation[4].isnumeric()
        if operation[3] == "*":
            self.operation = (operator.mul, operation[4])
        elif operation[3] == "+":
            self.operation = (operator.add, operation[4])
        test = params['Test'].strip().split()
        assert ' '.join(test[0:2]) == "divisible by"
        assert test[2].isnumeric()
        self.test_value = int(test[2])
        if_true = params['If true'].strip().split()
        assert ' '.join(if_true[0:3]) == "throw to monkey"
        assert if_true[3].isnumeric()
        self.monkey_when_true = int(if_true[3])
        if_false = params['If false'].strip().split()
        assert ' '.join(if_false[0:3]) == "throw to monkey"
        assert if_false[3].isnumeric()
        self.monkey_when_false = int(if_false[3])

    def inspect_item(self):
        self.inspection_count += 1
        return self.items.pop(0)

    def catch_item(self, worry):
        self.items.append(worry)

    def __repr__(self):
        def unoperator(op):
            if op is operator.mul:
                return "*"
            if op is operator.add:
                return "+"

        return f"Monkey {self.id}: items inspected: {self.inspection_count}, items: [{', '.join(map(str, self.items))}], operation: new = old {unoperator(self.operation[0])} {self.operation[1]}, test: divisible by {self.test_value}, true: throw to monkey {self.monkey_when_true}, false: {self.monkey_when_false} "


class Monkeys:
    def __init__(self, monkeydata):
        monkeys = [Monkey(m) for m in monkeydata]
        self.monkeys = {m.id: m for m in monkeys}

    def __repr__(self):
        return repr(self.monkeys)


def execute_round(monkeys):
    smooth_modulator = reduce(operator.mul, [monkey.test_value for monkey in monkeys.monkeys.values()])
    for _, monkey in sorted(monkeys.monkeys.items()):
        while len(monkey.items):
            worry = monkey.inspect_item()
            operation, value = monkey.operation
            value = worry if value == "old" else int(value)
            worry = operation(worry, value)
            worry %= smooth_modulator
            new_monkey = monkey.monkey_when_true if ((worry % monkey.test_value) == 0) else monkey.monkey_when_false
            monkeys.monkeys[new_monkey].catch_item(worry)


if __name__ == "__main__":
    # from io import StringIO
    # puzzle_input = StringIO("Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1\n")
    puzzle_input = open("day11.txt", "r")
    with puzzle_input as f:
        monkeys = f.read().split("\n\n")
    m = Monkeys(monkeys)
    for _ in range(10000):
        execute_round(m)
    monkey_counts = {monkey.inspection_count: number for number, monkey in m.monkeys.items()}
    top_monkey_counts = [k for k, v in sorted(monkey_counts.items(), reverse=True)[0:2]]
    print(f"Level of monkey business is: {top_monkey_counts[0] * top_monkey_counts[1]}")
