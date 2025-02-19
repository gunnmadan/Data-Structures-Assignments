from collections import deque
class Graph:
    def __init__(self):
        # A dictionary to store nodes by label
        self.nodes = {}

        # A dictionary to store adjacency list (node -> list of nodes)
        self.adjacency_list = {}


    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

    def add_node(self, label):
        node = self.Node(label)

        if label not in self.nodes:
            self.nodes[label] = node
            self.adjacency_list[node] = []

    def remove_node(self, label):
        node_to_remove = self.nodes.get(label)
        if node_to_remove is None:
            return
        for node in self.adjacency_list:
            if node_to_remove in self.adjacency_list[node]:
                self.adjacency_list[node].remove(node_to_remove)

        self.adjacency_list.pop(node_to_remove, None)
        self.nodes.pop(label, None)

    def add_edge(self, one, two):
        node_one = self.nodes.get(one)
        node_two = self.nodes.get(two)

        if node_one is None or node_two is None:
            raise ValueError("No such node exists!")

        self.adjacency_list[node_one].append(node_two)
        self.adjacency_list[node_two].append(node_one)

    def remove_edge(self, one, two):
        node_one = self.nodes.get(one)
        node_two = self.nodes.get(two)

        if node_one is None or node_two is None:
            return

        self.adjacency_list[node_one].remove(node_two)
        self.adjacency_list[node_two].remove(node_one)

    def are_adjacent(self, one, two):
        node_one = self.nodes.get(one)
        node_two = self.nodes.get(two)

        if node_one is None or node_two is None:
            return False

        return node_two in self.adjacency_list[node_one]

    def dfs_iterative(self, start_label):
        start_node = self.nodes.get(start_label)
        if start_node is None:
            return None
        traversal = []
        visited = set()
        stack = deque([start_node]) # deque as a stack

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal.append(node.label)

                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal


# Driver code
graph = Graph()

for label in ["A", "B", "C", "D", "E"]:
    graph.add_node(label)

# Adding edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")

print("DFS starting from node B:")
print(graph.dfs_iterative("B"))