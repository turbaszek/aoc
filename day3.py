from typing import List

from day1 import get_input


def part1(lines: List[str]):
    column_sums = {}
    half_size = len(lines) / 2
    for line in lines:
        for i, c in enumerate(list(line)):
            column_sums[i] = column_sums.get(i, 0) + int(line[i])

    gamma, epsilon = "", ""
    for i, column_sum in column_sums.items():
        bool_value = column_sum >= half_size
        gamma += str(int(bool_value))
        epsilon += str(int(not bool_value))

    g = int(gamma, base=2)
    e = int(epsilon, base=2)
    print(e * g)


def part2(input_lines: List[str]):
    def find_value(lines, predicate):
        idx = 0
        while len(lines) > 1:
            half_size = len(lines) / 2
            sum_ = sum(int(l[idx]) for l in lines)
            value = str(int(predicate(sum_, half_size)))
            lines = [l for l in lines if l[idx] == str(value)]
            idx += 1
        return int(lines[0], base=2)

    ox = find_value(list(input_lines), lambda s, h: s >= h)
    co = find_value(list(input_lines), lambda s, h: s < h)

    print(ox * co)


if __name__ == '__main__':
    lines = get_input(str)
    part1(lines)
    part2(lines)
