from typing import List

from utils import get_input


class Node:
    def __init__(
        self, name: str, is_directory: bool = False, size: int = 0, parent=None
    ):
        self.name = name
        self.is_directory = is_directory
        self.size = size
        self._children = {}
        self.parent = parent

    def add_child(self, ch: "Node"):
        ch.parent = self
        if self.is_directory:
            self.size += ch.size
        self._children[ch.name] = ch

    @property
    def children(self):
        return self._children.values()

    def show(self, level=0):
        print(
            level * " ",
            f"- {self.name} ({'dir' if self.is_directory else 'file'}) {self.size_of()}",
        )
        for ch in self.children:
            ch.show(level=level + 1)

    def __repr__(self):
        return f"Node({self.name})"

    def size_of(self):
        return self.size + sum(ch.size_of() for ch in self.children if ch.is_directory)


def build_directory_structure(ds: List[str]):
    current_directory = None
    for l in ds:
        if l.startswith("$ cd"):
            dir_name = l.replace("$ cd ", "")
            if dir_name == "..":
                current_directory = current_directory.parent
            else:
                if not current_directory:
                    current_directory = Node(dir_name, True)
                else:
                    new_directory = Node(dir_name, True)
                    current_directory.add_child(new_directory)
                    current_directory = new_directory
        elif l.startswith("$ ls"):
            continue
        elif l.startswith("dir"):
            current_directory.add_child(Node(l.replace("dir ", ""), True))
        else:
            size, name = l.split(" ")
            current_directory.add_child(Node(name, False, int(size)))
    while current_directory.parent:
        current_directory = current_directory.parent

    return current_directory


def bfs_search(node: Node, callback):
    queue = [node]
    while queue:
        current = queue.pop(0)
        callback(current)
        queue.extend(current.children)


def part1(current_directory: Node):
    class Counter:
        def __init__(self):
            self.total = 0

        def count_sum(self, current: Node):
            size = current.size_of()
            if current.is_directory and size <= 100000:
                self.total += size

    cnt = Counter()
    bfs_search(current_directory, cnt.count_sum)
    print(cnt.total)


def part2(current_directory: Node):
    class Search:
        def __init__(self, top_dir: Node):
            self.total = 70000000
            top_dir_size = top_dir.size_of()
            self.available = self.total - top_dir_size
            self.dir_to_remove_size = top_dir_size

        def search(self, curr: Node):
            if not curr.is_directory:
                return
            size = curr.size_of()
            if self.available + size >= 30000000 and size < self.dir_to_remove_size:
                self.dir_to_remove_size = size

    s = Search(current_directory)
    bfs_search(current_directory, s.search)
    print(s.dir_to_remove_size)


if __name__ == "__main__":
    ns = get_input()
    current_directory = build_directory_structure(ns)
    current_directory.show()
    part1(current_directory)
    part2(current_directory)
