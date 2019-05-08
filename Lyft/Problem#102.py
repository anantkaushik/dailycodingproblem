"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
"""
def subarraySum(nums, k):
    summ, d = 0, {}
    for i in range(len(nums)):
        summ += nums[i]
        if summ == k:
            return nums[:i+1]
        if summ - k in d:
            return nums[d[summ-k]+1:i+1]
        d[summ] = i