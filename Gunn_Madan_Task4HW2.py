   # 5 → 0 → 4
    #↑       ↓
   # 2 → 3 → 1

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort(self):
        visited = set()
        stack = []
        
        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
        
        for vertex in range(self.V):
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]
