from collections import Counter
from typing import List, NamedTuple

from utils import get_input, timeit


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
            signum(self.end.x - self.start.x),
            signum(self.end.y - self.start.y)
        )

    @classmethod
    def from_input(cls, line: str):
        s, e = line.strip().split(' -> ')
        s_x, s_y = s.split(",")
        e_x, e_y = e.split(",")
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
    cntr = Counter(all_points)
    print(sum(v >= 2 for v in cntr.values()))


def parse_input(input_lines: List[str]):
    return [Vector.from_input(l.strip()) for l in input_lines]


if __name__ == '__main__':
    assert Vector.from_input("1,1 -> 1,3").points() == [Point(x=1, y=1), Point(x=1, y=2), Point(x=1, y=3)]
    assert Vector.from_input("1,1 -> 3,1").points() == [Point(x=1, y=1), Point(x=2, y=1), Point(x=3, y=1)]

    vectors = parse_input(get_input(str))

    # Part 1
    with timeit():
        count(sum((v.points(no_diagonal=True) for v in vectors), start=[]))

    # Part 2
    with timeit():
        count(sum((v.points() for v in vectors), start=[]))
