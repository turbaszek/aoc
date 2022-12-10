from typing import List, Dict
from collections import deque
from utils import get_input


def execute_program(cmds: List[str]):
    cycle_history = {}
    cycle = 1
    register = 1
    queue = deque([])
    cmds = deque(cmds)
    while cmds or queue:
        if queue:
            register += queue.popleft()
        if cmds:
            queue.append(0)
            cmd = cmds.popleft()
            if cmd.startswith("addx"):
                _, value = cmd.split(" ")
                queue.append(int(value))
        cycle_history[cycle] = register
        cycle += 1

    return cycle_history


def part1(cycle_history: Dict[int, int]):
    s = 0
    for t in range(6):
        pos = 20 + 40 * t
        s += pos * cycle_history[pos]
    print(s)


def part2(cycle_history: Dict[int, int]):
    for k, v in cycle_history.items():
        end = "\n" if k % 40 == 0 else " "
        if v - 1 <= (k - 1) % 40 <= v + 1:
            print("#", end=end)
        else:
            print(".", end=end)


if __name__ == "__main__":
    ns = get_input()
    cycle_history = execute_program(ns)
    part1(cycle_history)
    part2(cycle_history)
