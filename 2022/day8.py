from dataclasses import dataclass
from typing import List, Dict, Tuple

from utils import get_input


@dataclass
class Node:
    height: int
    visible: bool = False


def build_graph(grid: List[List[int]]):
    graph: Dict[Tuple[int, int], Node] = {}

    for row_i, row in enumerate(grid):
        for col_i, col in enumerate(row):
            graph[(row_i, col_i)] = Node(col)
    print("done")
    return graph


def iterate1(n: Node, graph: Dict[Tuple[int, int], Node], func):
    idx = 1
    while True:
        node = graph.get(func(idx))
        if not node:
            return True
        if node.height >= n.height:
            return False
        idx += 1


def part1(graph: Dict[Tuple[int, int], Node]):
    visible = 0
    for (x, y), current_node in graph.items():
        if any(
            [
                iterate1(current_node, graph, lambda i: (x, y + i)),
                iterate1(current_node, graph, lambda i: (x, y - i)),
                iterate1(current_node, graph, lambda i: (x + i, y)),
                iterate1(current_node, graph, lambda i: (x - i, y)),
            ]
        ):
            visible += 1
    print(visible)


def count_trees(n: Node, graph: Dict[Tuple[int, int], Node], func):
    idx = 1
    while True:
        node = graph.get(func(idx))
        if not node:
            return idx - 1
        if node and node.height < n.height:
            idx += 1
        elif node and node.height == n.height:
            return idx
        else:
            return idx


def part2(graph: Dict[Tuple[int, int], Node]):
    scores = {}
    for (x, y), current_node in graph.items():
        value = 1

        value *= count_trees(current_node, graph, lambda i: (x, y + i))
        value *= count_trees(current_node, graph, lambda i: (x, y - i))
        value *= count_trees(current_node, graph, lambda i: (x + i, y))
        value *= count_trees(current_node, graph, lambda i: (x - i, y))
        scores[(x, y)] = value

    print(max(scores.values()))


if __name__ == "__main__":
    ns = get_input()
    grid = [list(map(int, l)) for l in ns]
    graph = build_graph(grid)

    part1(graph)
    part2(graph)
