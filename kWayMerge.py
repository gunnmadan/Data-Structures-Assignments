import heapq

def k_way_merge(lists):
    # Initialize a min-heap
    min_heap = []

    # Add the first element of each list to the heap
    for i in range(len(lists)):
        sorted_list = lists[i]
        if sorted_list:  # Check if the list is not empty
            heapq.heappush(min_heap, (sorted_list[0], i, 0))  # (value, list index, element index)

    res = []

    while min_heap:
        # Get the smallest element from the heap
        value, list_idx, elem_idx = heapq.heappop(min_heap)
        res.append(value)

        # If there is a next element in the same list, add it to the heap
        if elem_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, elem_idx + 1))

    return res


# Example usage
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6],
    [0, 7, 8]
]

result = k_way_merge(lists)
print(result)
