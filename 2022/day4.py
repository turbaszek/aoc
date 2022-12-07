from typing import List, NamedTuple
import string
from utils import get_input


class Range(NamedTuple):
    lower: int
    upper: int

    def contains(self, other: "Range"):
        return self.lower <= other.lower and other.upper <= self.upper

    def overlaps(self, other: "Range"):
        return (self.lower <= other.lower <= self.upper) or (
            self.lower <= other.upper <= self.upper
        )

    @classmethod
    def from_string(cls, inp: str):
        a, b = inp.split("-")
        return cls(int(a), int(b))


def part1(ns: List[str]):
    contains = 0
    overlaps = 0
    for n in ns:
        a, b = n.split(",")
        ar = Range.from_string(a)
        br = Range.from_string(b)
        if ar.contains(br) or br.contains(ar):
            contains += 1
        if ar.overlaps(br) or br.overlaps(ar):
            overlaps += 1
    print(contains)
    print(overlaps)


def part2(ns: List[str]):
    pass


if __name__ == "__main__":
    ns = get_input()
    print(len(ns))
    #     ns = """2-4,6-8
    # 2-3,4-5
    # 5-7,7-9
    # 2-8,3-7
    # 6-6,4-6
    # 2-6,4-8
    # 3-19,19-98""".splitlines(keepends=False)
    part1(ns)
    part2(ns)
