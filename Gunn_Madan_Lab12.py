import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)] # (distance, node)
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if current_dist > distances[u]:
                continue

            for v, weight in graph[u]:
                distance = current_dist + weight

                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(min_heap, (distance, v))
        max_dist = max(distances.values())
        return max_dist if max_dist != float('inf') else -1

# Example usage: 
times1 = [[2,1,1],[2,3,1],[3,4,1]] 
n1 = 4 
k1 = 2 
print(Solution().networkDelayTime(times1, n1, k1))        

