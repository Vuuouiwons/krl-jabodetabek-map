import logging
from collections import deque

from .Node import Node

if __name__ == '__main__':
    raise RuntimeError('This is a module package')

logger = logging.getLogger(__name__)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value: str) -> Node:
        if value not in self.nodes:
            self.nodes[value] = Node(value)

        return self.nodes[value]

    def add_edge(self, from_value: str, to_value: str, weight: int = 0) -> None:
        from_node = self.add_node(from_value)
        to_node = self.add_node(to_value)

        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)

    def display(self) -> None:
        seen = set()
        for node in self.nodes.values():
            for neighbor, weight in node.edges:
                key = tuple(sorted([node.value, neighbor.value]))
                if key not in seen:
                    logger.info(
                        f"{node.value} -> {neighbor.value} (w={weight})")
                    seen.add(key)

    def bfs(self, start_value: str, end_value: str) -> tuple[list[Node], int] | None:
        if start_value not in self.nodes or end_value not in self.nodes:
            logger.info("Start or end node not found in the graph.")
            return

        visited = set()
        queue = deque()
        # (current_node, path_so_far, total_weight)
        queue.append((self.nodes[start_value], [start_value], 0))

        while queue:
            current_node, path, total_weight = queue.popleft()

            if current_node.value == end_value:
                logger.info(
                    f"Path found: {' -> '.join(path)} (Total weight: {total_weight})")
                return path, total_weight

            if current_node.value in visited:
                continue

            visited.add(current_node.value)

            for neighbor, weight in current_node.edges:
                if neighbor.value not in visited:
                    queue.append(
                        (neighbor, path + [neighbor.value], total_weight + weight))

        logger.info(f"No path found from {start_value} to {end_value}.")
        return None, float('inf')
