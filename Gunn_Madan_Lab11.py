def extract_cycle(adj_list, start):
    def dfs(node, path, visited):
        if node in visited:
            cycle_start_index = path.index(node)
            return path[cycle_start_index:] + [node]
        visited.add(node)
        path.append(node)
        for neighbor in adj_list[node]:
            result = dfs(neighbor, path, visited)
            if result:
                return result
        path.pop()
        visited.remove(node)
        return []

    return dfs(start, [], set())

# Adjacency list representing the graph
adj = [
    [1, 3],
    [2],
    [4],
    [],
    [0, 3],
    [2]
]

print(extract_cycle(adj, 0))  # Should print [0, 1, 2, 4, 0]
print(extract_cycle(adj, 1))  # Should print [1, 2, 4, 0, 1]
print(extract_cycle(adj, 3))  # Should print []
