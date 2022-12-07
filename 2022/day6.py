from typing import List

from utils import get_input


def process_stream(stream: List[str], buffer_length: int):
    buffer = []
    for idx, d in enumerate(stream):
        if len(buffer) == buffer_length:
            buffer.pop(0)
        buffer.append(d)
        if len(set(buffer)) == buffer_length:
            print(idx + 1)
            return


def part1(ds: List[str]):
    process_stream(ds, 4)


def part2(ds: List[str]):
    process_stream(ds, 14)


if __name__ == "__main__":
    ns = get_input()
    part1(list(ns[0]))
    part2(list(ns[0]))
