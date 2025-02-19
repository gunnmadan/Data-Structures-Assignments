import heapq


def dijkstra(graph, start):
    # Initialize the distances
    shortest = {node: float('inf') for node in graph}
    shortest[start] = 0
    prev = {node: None for node in graph}

    # A min priority queue to maintain the node with min distance
    min_pq = [(0, start)]  # (distance, node)

    while min_pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(min_pq)

        # If the current distance is already greater than the shortest, skip
        if current_distance > shortest[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < shortest[neighbor]:
                shortest[neighbor] = new_distance
                prev[neighbor] = current_node
                heapq.heappush(min_pq, (new_distance, neighbor))

    return shortest

def get_shortest_path(prev, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = prev[current_node]

    path.reverse()

    return path


# Driver Code
weightedGraph = {
    '0': [('1', 2), ('2', 8)],
    '1': [('0', 2), ('5', 7)],
    '2': [('0', 8), ('3', 4), ('4', 2)],
    '3': [('0', 3), ('2', 4), ('4',1)],
    '4': [('2', 2), ('3', 1), ('5',12)],
    '5': [('4', 12), ('1', 7)]
}


#  shortest paths from node '2'
distances = dijkstra(weightedGraph, '2')
print(distances)

