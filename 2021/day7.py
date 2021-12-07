from typing import List

from utils import get_input


def solve(positions: List[int], summator):
    position_map = {i: 0 for i in range(max(positions) + 1)}
    for p in positions:
        position_map[p] += 1

    positions_costs = {}
    for p in position_map:
        cost = 0
        for x, count in position_map.items():
            if x != p:
                cost += summator(abs(p - x), count)
        positions_costs[p] = cost

    print(min(positions_costs.values()))


if __name__ == "__main__":
    positions = [int(n) for n in get_input(str)[0].split(",")]

    solve(positions, lambda s, c: s * c)
    solve(positions, lambda s, c: (1 + s) / 2 * s * c)
