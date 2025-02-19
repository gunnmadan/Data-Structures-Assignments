 class Heap:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.size = 0

    def is_full(self):
        return self.size == len(self.items)

    def is_empty(self):
        return self.size == 0

    def insert(self, value):
        if self.is_full():
            raise Exception("Heap is full")

        self.items[self.size] = value
        self.size += 1

        # Bubble up from the last index (newly added element)
        self.bubble_up(self.size-1)

    def bubble_up(self, i):
        parent = (i - 1) // 2  # index of the parent node

        # Check if the current node is smaller than its parent, swap if needed
        if i > 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            self.bubble_up(parent) # Recursively bubble up from the parent's index

    def remove(self):
        if self.is_empty():
            raise Exception("Heap is empty")

        root = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.bubble_down(0)
        return root

    def bubble_down(self, i):
        l = 2 * i + 1  # Left child index
        r = 2 * i + 2  # Right child index

        smallest = i  # Assume the smallest is the current index

        # Check if the left child exists and is smaller than the current
        if l < self.size and self.items[l] < self.items[smallest]:
            smallest = l

        # Check if the right child exists and is smaller than the current smallest
        if r < self.size and self.items[r] < self.items[smallest]:
            smallest = r

        # If the smallest is not the current index, swap
        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.bubble_down(smallest)  # And, recursively bubble down the affected child

import random

size = 12
arr = [0] * size

for i in range(size):
    arr[i] = random.randint(0, 99)
print('Original array: ', arr)

def heap_sort(arr):
    heap = Heap(size)

    for i in range(size):
        heap.insert(arr[i])

    for i in range(size):
        arr[i] = heap.remove()

heap_sort(arr)
print('Sorted array: ',arr)
