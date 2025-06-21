if __name__ == '__main__':
    raise RuntimeError('This is a module package')


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []  # list of (neighbor, weight)

    def add_edge(self, neighbor, weight=1):
        self.edges.append((neighbor, weight))

    def __repr__(self):
        return f"Node({self.value}), Edge({self.edges})"