from typing import List
import string
from utils import get_input


def priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def part1(ns: List[str]):
    items = []
    for n in ns:
        l = int(len(n) / 2)
        letter: str = set(n[0:l]).intersection(set(n[l:])).pop()
        items.append(priority(letter))

    print(sum(items))


def part2(ns: List[str]):
    i = 0
    items = []
    group = []
    for n in ns:
        group.append(set(n))
        if i < 2:
            i += 1
            continue
        else:
            common = group[0].intersection(group[1]).intersection(group[2])
            items.append(priority(common.pop()))
            i = 0
            group = []
    print(sum(items))


if __name__ == "__main__":
    ns = get_input()
    #     ns = """vJrwpWtwJgWrhcsFMMfFFhFp
    # jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    # PmmdzqPrVvPwwTWBwg
    # wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    # ttgJtRGJQctTZtZT
    # CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines(keepends=False)
    print(ord("a"))
    print(ord("A"))
    print(ord("B"))
    part1(ns)
    part2(ns)
