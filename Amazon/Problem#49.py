"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 
42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.
"""
def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    Sum = 0
    result = Sum 
    for i in range(len(nums)):
        Sum = (Sum + nums[i]) if(Sum+nums[i]) >= nums[i] else nums[i]
        result = Sum if Sum > result else result
    return result