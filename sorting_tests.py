import numpy as np
import pdb

def sum(n):
    if (n == 0):
        return 0
    return n + sum(n - 1)

# print(sum(500000000))

def sum_iter(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# print(sum_iter(500000000))


def max_min_values(arr):
    max_value = arr[0]   
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]
    return max_value, min_value

# print(max_min_values([100, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Example usage   
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)        
