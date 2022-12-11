import re
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List, Dict
from utils import get_input


@dataclass
class Value:
    value: int
    div_rests: Dict[int, int] = field(default_factory=dict)

    def _update_rests(self, func):
        for k in list(self.div_rests):
            self.div_rests[k] = func(k)

    def init(self, by: int):
        self.div_rests[by] = self.value % by

    def is_divisible(self, by: int):
        return self.div_rests[by] == 0

    def process(self, operation: str):
        if operation == "old * old":
            self.pow()
            return

        match = re.findall(r"old ([\+, \*]) (\d+)", operation)
        op, value = match[0]
        if op == "+":
            self.add(int(value))
        elif op == "*":
            self.multiply(int(value))

    def pow(self):
        # (xk + r)(xk + r) = (xk)^ + 2xkr + r^ = xk(xk + 2r) + r^
        self._update_rests(lambda k: (self.div_rests[k] * self.div_rests[k]) % k)

    def multiply(self, value):
        # (xk + r)b = xkb + rb
        self._update_rests(lambda k: (self.div_rests[k] * value) % k)

    def add(self, value):
        # (xk + r) + b = xkb + (r + b)
        self._update_rests(lambda k: (self.div_rests[k] + value) % k)


@dataclass
class Monkey:
    name: int
    operation: str
    div_by: int
    test_positive: int
    test_negative: int
    queue: List[Value] = field(default_factory=list)
    inspected: int = 0

    @staticmethod
    def _value_from_re(pattern: str, source: str):
        return re.findall(pattern, source)[0]

    @classmethod
    def from_input(cls, monkey_input):
        raw_name, raw_queue, raw_op, raw_div, raw_pos, raw_neg = monkey_input
        name = cls._value_from_re(r"Monkey (\d+):", raw_name)
        queue = [Value(int(x)) for x in raw_queue.split(":")[1].split(",")]
        operation = raw_op.split(":")[1].split("=")[1].strip()
        div = cls._value_from_re(r"Test: divisible by (\d+)", raw_div)
        test_positive = cls._value_from_re(r"If true: throw to monkey (\d+)", raw_pos)
        test_negative = cls._value_from_re(r"If false: throw to monkey (\d+)", raw_neg)
        return cls(
            int(name),
            operation,
            int(div),
            int(test_positive),
            int(test_negative),
            queue,
        )

    def process1(self, monkeys: Dict[int, "Monkey"]):
        while self.queue:
            self.inspected += 1
            value = self.queue.pop(0)
            nw = eval(self.operation, {"old": value.value})
            new_value = Value(int(nw / 3))
            if new_value.value % self.div_by == 0:
                monkeys[self.test_positive].queue.append(new_value)
            else:
                monkeys[self.test_negative].queue.append(new_value)

    def process2(self, monkeys: Dict[int, "Monkey"]):
        while self.queue:
            self.inspected += 1
            value = self.queue.pop(0)
            value.process(self.operation)
            if value.is_divisible(self.div_by):
                monkeys[self.test_positive].queue.append(value)
            else:
                monkeys[self.test_negative].queue.append(value)


def parse_input(ns: List[str]):
    monkey_input = []
    monkeys = {}
    while ns:
        line = ns.pop(0)
        if line != "":
            monkey_input.append(line.strip())
        else:
            m = Monkey.from_input(monkey_input)
            monkeys[m.name] = m
            monkey_input = []

    m = Monkey.from_input(monkey_input)
    monkeys[m.name] = m
    return monkeys


def part1(monkeys: Dict[int, Monkey]):
    for _ in range(20):
        for monkey in monkeys.values():
            monkey.process1(monkeys)

    monkey_score(monkeys)


def part2(monkeys: Dict[int, Monkey]):
    db = [m.div_by for m in monkeys.values()]
    for monkey in monkeys.values():
        for v in monkey.queue:
            for d in db:
                v.init(d)

    for _ in range(10000):
        for monkey in monkeys.values():
            monkey.process2(monkeys)

    monkey_score(monkeys)


def monkey_score(monkeys):
    a, b = sorted([m.inspected for m in monkeys.values()])[-2:]
    print(a * b)


if __name__ == "__main__":
    ns = get_input()
    ms = parse_input(ns)
    part1(deepcopy(ms))
    part2(deepcopy(ms))
