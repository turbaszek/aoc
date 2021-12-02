import os
from typing import List

import requests
from datetime import datetime

AOC_SESSION = 'AOC_SESSION'
CACHE_NAME_TMPL = "tomek_day{}.cache"


def cache(key: int, txt: str) -> None:
    with open(CACHE_NAME_TMPL.format(key), "w+") as f:
        f.write(txt)


def check_cache(key: int) -> str:
    with open(CACHE_NAME_TMPL.format(key), "r") as f:
        txt = f.read()
    return txt


def get_input_from_cache(day: int) -> str:
    return check_cache(day)


def get_input_from_aoc(day: int) -> str:
    url = "https://adventofcode.com/2021/day/{}/input"
    r = requests.get(
        url.format(day),
        headers={"Cookie": f"session={os.environ[AOC_SESSION]}"}
    )
    r.raise_for_status()
    return r.text


def get_input(cast_to=None) -> List:
    day = datetime.now().day

    try:
        txt = get_input_from_cache(day)
    except FileNotFoundError:
        txt = get_input_from_aoc(day)
        cache(day, txt)

    cast = cast_to or str
    return [cast(x) for x in txt.splitlines(keepends=False)]


def part1(ns):
    print(sum(a < b for a, b in zip(ns[:-1], ns[1:])))


def part2(ns):
    i = 2
    ma = []
    while i < len(ns):
        ma.append(sum([ns[i-2], ns[i-1], ns[i]]))
        i += 1
    return ma


if __name__ == '__main__':
    ns = get_input(int)
    part1(ns)
    part1(part2(ns))

