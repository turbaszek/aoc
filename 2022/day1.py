from typing import List

from utils import get_input


def part1(ns: List[str]):
    mxs = []
    agg = 0
    for n in ns:
        print(n)
        if n != "":
            agg += int(n)
        else:
            mxs.append(agg)
            agg = 0
    print(max(mxs))
    return mxs


def part2(mxs: List[int]):
    mxs.sort(reverse=True)
    print(mxs)
    print(sum(mxs[:3]))


if __name__ == "__main__":
    ns = get_input()
    part1(ns)
    part2(part1(ns))
