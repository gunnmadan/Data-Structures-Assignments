for i in range(n):
    sum = 0
    for j in range(n):
        for k in range(n):
            sum = sum + a_vals[i][k] * b_vals[k][j]
        c_vals[i][j] = sum

def square_numbers(nums):
    squared_nums = []

    for num in nums:
        squared _nums.append(num * num)

    return squared_nums
