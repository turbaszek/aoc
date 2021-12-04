from typing import List

from day1 import get_input


class Number:
    def __init__(self, x: int, y: int, n: int):
        self.x = x
        self.y = y
        self.n = n
        self.marked = False

    def __repr__(self):
        return f"N(x: {self.x}, y: {self.y}, n: {self.n})"

    def mark(self, n: int) -> None:
        if n == self.n:
            self.marked = True


class Board:
    def __init__(self, rows: List[List[str]]):
        self._numbers = []
        for y, r in enumerate(rows):
            for x, n in enumerate(r):
                self._numbers.append(Number(x, y, int(n)))

        self.winner = False

    def mark(self, n: int) -> None:
        for number in self._numbers:
            number.mark(n)

    def check_wins(self) -> bool:
        columns = {i: 0 for i in range(5)}
        rows = {i: 0 for i in range(5)}
        for n in self._numbers:
            columns[n.x] += int(n.marked)
            rows[n.y] += int(n.marked)
        if any(c == 5 for c in columns.values()) or any(r == 5 for r in rows.values()):
            self.winner = True
        return self.winner

    def score(self, n) -> int:
        return sum([x.n for x in self._numbers if not x.marked]) * n


def parse_input(lines: List[str]):
    numbers = map(int, lines.pop(0).split(","))
    lines.pop(0)

    boards = []
    tmp_rows = []
    while lines:
        line = lines.pop(0)
        if line == "":
            boards.append(Board(tmp_rows))
            tmp_rows = []
            continue
        tmp_rows.append(line.replace("  ", " ").strip().split(" "))

    boards.append(Board(tmp_rows))

    return numbers, boards


def solve(input_lines: List[str]):
    ns, bs = parse_input(input_lines)
    winners: List[int] = []
    first_winner_score = None

    for n in ns:
        bs_copy = list(bs)
        bs = []
        for b in bs_copy:
            b.mark(n)
            if b.check_wins():
                first_winner_score = first_winner_score or b.score(n)
                winners.append(b.score(n))
            else:
                bs.append(b)

    print("Part 1:", first_winner_score)
    print("Part 2:", winners[-1])


if __name__ == '__main__':
    lines = get_input(str)
    solve(lines)
