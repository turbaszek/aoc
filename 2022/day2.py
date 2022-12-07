from typing import List

from utils import get_input


move_map = {"X": "A", "Y": "B", "Z": "C"}
move_points = {"A": 1, "B": 2, "C": 3}

winning = [("A", "B"), ("B", "C"), ("C", "A")]
winning_shapes = {"A": "B", "B": "C", "C": "A"}
loosing_shapes = {"A": "C", "B": "A", "C": "B"}


def is_win(a, b):
    b = move_map[b]
    if a == b:
        return move_points[b] + 3
    if (a, b) in winning:
        return move_points[b] + 6
    return move_points[b]


def make_a_move(a, b):
    if b == "X":
        return move_points[loosing_shapes[a]]
    if b == "Y":
        return move_points[a] + 3
    return move_points[winning_shapes[a]] + 6


def part1(ns: List[str]):
    points = 0
    for line in ns:
        a, b = line.split(" ")
        points += is_win(a, b)
    print(points)


def part2(ns: List[str]):
    points = 0
    for line in ns:
        a, b = line.split(" ")
        points += make_a_move(a, b)
    print(points)


if __name__ == "__main__":
    ns = get_input()
    part1(ns)
    part2(ns)
