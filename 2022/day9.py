from dataclasses import dataclass
from typing import List

from utils import get_input


def sig(n: int):
    if n == 0:
        return 0
    return 1 if n > 0 else -1


@dataclass
class Position:
    x: int
    y: int
    next_node: "Position" = None

    def move(self, move: str):
        if move == "U":
            self.y += 1
        elif move == "D":
            self.y -= 1
        elif move == "L":
            self.x -= 1
        elif move == "R":
            self.x += 1

    def distance(self, other):
        return max([abs(self.x - other.x), abs(self.y - other.y)])

    def need_to_move(self, other):
        return self.distance(other) > 1

    def move_tail(self):
        next_node = self.next_node

        if not next_node:
            return

        if self.distance(next_node) > 1:
            dx = self.x - next_node.x
            dy = self.y - next_node.y
            next_node.x = next_node.x + sig(dx)
            next_node.y = next_node.y + sig(dy)
            next_node.move_tail()

    def tail(self):
        last = self
        while last.next_node:
            last = last.next_node
        return last.x, last.y


def calculate(head: Position, ns: List[str]):
    tail_pos = set()
    for n in ns:
        move, step = n.split(" ")
        for _ in range(int(step)):
            head.move(move)
            head.move_tail()
            tail_pos.add(head.tail())

    print(len(tail_pos))


def part1(ns: List[str]):
    head = Position(0, 0)
    tail = Position(0, 0)
    head.next_node = tail
    calculate(head, ns)


def part2(ns: List[str]):
    head = Position(0, 0)
    tail = Position(0, 0)
    head.next_node = tail
    for _ in range(8):
        new = Position(0, 0)
        tail.next_node = new
        tail = new
    calculate(head, ns)


if __name__ == "__main__":
    ns = get_input()
    part1(ns)
    part2(ns)
