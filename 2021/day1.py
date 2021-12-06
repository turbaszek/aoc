from typing import List

from utils import get_input


def part1(ns: List[int]):
    print(sum(a < b for a, b in zip(ns[:-1], ns[1:])))


def part2(ns: List[int]):
    i = 2
    ma = []
    while i < len(ns):
        ma.append(sum([ns[i - 2], ns[i - 1], ns[i]]))
        i += 1
    return ma


if __name__ == "__main__":
    ns = get_input(int)
    part1(ns)
    part1(part2(ns))
