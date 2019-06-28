"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
Do this in O(N) time.
"""
def getSmallest(arr):
    res = 1
    for no in arr:
        if res >= no:
            res += no
        else:
            return res
    return res