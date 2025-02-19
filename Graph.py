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

    def bfs(self, start_label):
        start_node = self.nodes.get(start_label)
        if start_node is None:
            return None

        traversal = []
        visited = set()  # Set of visited nodes
        queue = deque()  # Queue for BFS
        queue.append(start_node)

        while queue:
            current_node = queue.popleft()  # Dequeue the front node
            if current_node not in visited:
                visited.add(current_node)
                traversal.append(current_node.label)

                for neighbor in self.adjacency_list[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # Add unvisited neighbors to the queue

        return traversal

    def isReachable(self, one, two):
        start_node = self.nodes.get(one)
        target_node = self.nodes.get(two)
        if start_node is None or target_node is None:
            return False
            
        visited = set()
        queue = deque([start_node])
        
        while queue:
            current = queue.popleft()
            if current == target_node:
                return True
            visited.add(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    
        return False

    def numConnectedComponents(self):
        visited = set()
        count = 0
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in self.adjacency_list[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            
        for node in self.nodes.values():
            if node not in visited:
                dfs(node)
                count += 1
                
        return count

# Driver code
graph = Graph()

for label in ["A", "B", "C", "D", "E", "F"]:
    graph.add_node(label)

# Adding edges
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("D", "E")
graph.add_edge("E", "F")

print(graph.isReachable("A","C")) # should print 'True'
print(graph.isReachable("A","F")) # should print 'False'
print(graph.numConnectedComponents()) # should print '2'
