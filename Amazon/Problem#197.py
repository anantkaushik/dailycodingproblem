"""
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
"""
def rotate(nums, k):
    k = k % len(nums)
    count = start = 0
    while count < len(nums):
        cur = start
        prev = nums[start]
        while True:
            nextIndex = (cur + k) %len(nums)
            nums[nextIndex], prev = prev, nums[nextIndex]
            cur = nextIndex
            count += 1
            if start == cur:
                break
        start += 1