from functools import reduce
from typing import NamedTuple, List

from day1 import get_input


class Result(NamedTuple):
    forward: int = 0
    depth: int = 0
    aim: int = 0


def part1(lines: List[str]):
    def mapper(line: str) -> Result:
        type_, value = line.split(" ")
        result_map = {
            "forward": lambda v: Result(v),
            "down": lambda v: Result(0, v),
            "up": lambda v: Result(0, -v),
        }
        return result_map[type_](int(value))

    def reducer(a: Result, b: Result):
        return Result(a.forward + b.forward, a.depth + b.depth)

    r = reduce(reducer, map(mapper, lines))
    print(r.forward * r.depth)


def part2(lines: List[str]):
    f, d, a = 0, 0, 0
    for l in lines:
        type_, value = l.split(" ")
        value = int(value)
        if type_ == "forward":
            f += value
            d += a * value
        elif type_ == "down":
            a += value
        elif type_ == "up":
            a -= value
    print(f, d, f * d)


if __name__ == '__main__':
    lines = get_input(str)
    part1(lines)
    part2(lines)
