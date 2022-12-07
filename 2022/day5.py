import re
from copy import copy
from typing import List, NamedTuple
from utils import get_input


class Command(NamedTuple):
    num: int
    origin: int
    dest: int


def parse_command(cmd: str):
    match = re.findall("move (\d+) from (\d) to (\d)", cmd)
    return Command(*[int(x) for x in match[0]])


def move_container_9000(state, cmd: Command):
    for _ in range(cmd.num):
        c = state[cmd.origin].pop()
        state[cmd.dest].append(c)
        print(f"moved {c} from {cmd.origin} to {cmd.dest}")


def move_container_9001(state, cmd: Command):
    cnts = []
    for _ in range(cmd.num):
        c = state[cmd.origin].pop()
        cnts.insert(0, c)
    for cnt in cnts:
        state[cmd.dest].append(cnt)

    print(f"moved {cnts} from {cmd.origin} to {cmd.dest}")


def run_the_crane(state: dict, cmds: List[str], func):
    for cmd in cmds:
        if cmd.startswith("move"):
            func(state, parse_command(cmd))

    print("".join([state[s][-1] for s in state]))


def part1(state: dict, ns: List[str]):
    run_the_crane(state, ns, move_container_9000)


def part2(state, ns: List[str]):
    run_the_crane(state, ns, move_container_9001)


def parse_initial_state(txt: str):
    state = {}
    for line in txt.splitlines(keepends=False):
        for m in re.finditer("([\w])+", line):
            curr = state.get(m.start(), [])
            curr.insert(0, m.group(0))
            state[m.start()] = curr

    new_state = {}
    for idx, key in enumerate(sorted(state.keys())):
        new_state[idx + 1] = state[key]

    return new_state


if __name__ == "__main__":
    initial = """
[D]                     [N] [F]    
[H] [F]             [L] [J] [H]    
[R] [H]             [F] [V] [G] [H]
[Z] [Q]         [Z] [W] [L] [J] [B]
[S] [W] [H]     [B] [H] [D] [C] [M]
[P] [R] [S] [G] [J] [J] [W] [Z] [V]
[W] [B] [V] [F] [G] [T] [T] [T] [P]
[Q] [V] [C] [H] [P] [Q] [Z] [D] [W]
 """
    initial_state = parse_initial_state(initial)
    ns = get_input()
    print(len(ns))

    part1(copy(initial_state), ns)
    part2(copy(initial_state), ns)
