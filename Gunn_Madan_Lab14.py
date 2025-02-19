def counting_sort(arr, min_value, max_value):
    # Create a count array to store the frequency of each element
    count = [0] * (max_value - min_value + 1)
    
    # Count occurrences of each element in the input array
    for num in arr:
        count[num - min_value] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i + min_value] * freq)
    
    return sorted_arr

#Array 1: [527, 8763, 12, 45, 9076, 298, 7603, 432, 1, 30456]
#Analysis: Not recommended due to a large range of values

#Array2: [10, 5, 7, 12, 8, 5, 14, 15, 6, 13]
#Analysis: Recommended as the range is small and the size is reasonable

#Array3: [2300, 2298, 2299, 2302, 2307, 2305, 2304, 2302, 2306, 2303]
#Analysis: Recommended as the range is small and the size is reasonable. 

