import heapq

class PercentileMonitor:
    def __init__(self):
        self.lower_25 = []  # Max-Heap (invert signs for max-heap)
        self.upper_25 = []  # Min-Heap
        self.lower_75 = []  # Max-Heap
        self.upper_75 = []  # Min-Heap
        self.total_count = 0  # Total number of elements
    
    def add(self, num):
        self.total_count += 1  # Increment total count
        
        # Add to 25th percentile heaps
        if not self.lower_25 or num <= -self.lower_25[0]:
            heapq.heappush(self.lower_25, -num)
        else:
            heapq.heappush(self.upper_25, num)
        self._balance_25()
        
        # Add to 75th percentile heaps
        if not self.lower_75 or num <= -self.lower_75[0]:
            heapq.heappush(self.lower_75, -num)
        else:
            heapq.heappush(self.upper_75, num)
        self._balance_75()
    
    def _balance_25(self):
        # Target size for lower_25 is ceil(25% of total_count)
        target_size = (self.total_count + 3) // 4  # +3 ensures correct rounding for small counts
        
        while len(self.lower_25) > target_size:
            heapq.heappush(self.upper_25, -heapq.heappop(self.lower_25))
        while len(self.lower_25) < target_size:
            heapq.heappush(self.lower_25, -heapq.heappop(self.upper_25))
    
    def _balance_75(self):
        # Target size for lower_75 is ceil(75% of total_count)
        target_size = (3 * self.total_count + 3) // 4  # +3 ensures correct rounding for small counts
        
        while len(self.lower_75) > target_size:
            heapq.heappush(self.upper_75, -heapq.heappop(self.lower_75))
        while len(self.lower_75) < target_size:
            heapq.heappush(self.lower_75, -heapq.heappop(self.upper_75))
    
    def get_25th(self):
        # Return the largest element in lower_25 (25th percentile)
        return -self.lower_25[0] if self.lower_25 else None
    
    def get_75th(self):
        # Return the smallest element in upper_75 (75th percentile)
        return self.upper_75[0] if self.upper_75 else None


data = [13, 24, 28, 32, 33, 39, 40, 45, 46, 55, 56, 57, 58, 59, 60, 67, 68, 71, 74, 75, 80, 83, 84, 89, 90]
pm = PercentileMonitor()
for num in data:
    pm.add(num)

print("25th Percentile:", pm.get_25th())  # Expected: 40
print("75th Percentile:", pm.get_75th())  # Expected: 74
