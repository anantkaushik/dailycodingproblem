"""
Given an array of integers, return a new array such that each element at index i of the new array is the 
product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
def productExceptSelf(nums):
    p = 1
    n = len(nums)
    result = []
    for i in range(0,n):
        result.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
        result[i] = result[i] * p
        p = p * nums[i]
    return result
