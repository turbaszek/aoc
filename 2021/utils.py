import os
import time
from datetime import datetime
from typing import List
from contextlib import contextmanager
import requests

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


@contextmanager
def timeit():
    start = time.monotonic_ns()
    yield
    end = time.monotonic_ns()
    print(f"Time: {(end - start)/1000000} ms")
