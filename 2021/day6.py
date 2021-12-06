from typing import List

from utils import get_input


def solve(fishes: List[int], days: int):
    fish_to_count_map = {i: 0 for i in range(9)}

    for fish in fishes:
        fish_to_count_map[fish] += 1

    for _ in range(days):
        for k, v in list(fish_to_count_map.items()):
            if k == 0:
                fish_to_count_map[6] = fish_to_count_map[8] = v
            elif k == 7:
                fish_to_count_map[k-1] += v
            else:
                fish_to_count_map[k-1] = v

    print(sum(fish_to_count_map.values()))


if __name__ == '__main__':
    fishes = [int(n) for n in get_input(str)[0].split(",")]

    solve(fishes, 80)
    solve(fishes, 256)
