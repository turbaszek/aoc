import re
from collections import Counter
from typing import List, NamedTuple

from utils import get_input, timeit


PATTERN = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")


def signum(n: float):
    return bool(n > 0) - bool(n < 0)


class Point(NamedTuple):
    x: int
    y: int


class Vector:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.direction_vector = Point(
            signum(self.end.x - self.start.x), signum(self.end.y - self.start.y)
        )

    @classmethod
    def from_input(cls, line: str):
        s_x, s_y, e_x, e_y = re.findall(PATTERN, line)[0]
        return cls(Point(int(s_x), int(s_y)), Point(int(e_x), int(e_y)))

    def points(self, no_diagonal: bool = False) -> List[Point]:
        points = []

        if no_diagonal and self.direction_vector.x * self.direction_vector.y != 0:
            return points

        points.append(self.start)
        s = self.start
        while s != self.end:
            s = Point(s.x + self.direction_vector.x, s.y + self.direction_vector.y)
            points.append(s)

        return points


def count(all_points: List[Point]):
    print(sum(v >= 2 for v in Counter(all_points).values()))


def parse_input(input_lines: List[str]):
    return [Vector.from_input(l.strip()) for l in input_lines]


if __name__ == "__main__":
    vectors = parse_input(get_input(str))

    # Part 1
    with timeit():
        count(sum((v.points(no_diagonal=True) for v in vectors), start=[]))

    # Part 2
    with timeit():
        count(sum((v.points() for v in vectors), start=[]))
