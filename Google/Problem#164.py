"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, 
there must be a duplicate. Find it in linear time and space.
"""
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1