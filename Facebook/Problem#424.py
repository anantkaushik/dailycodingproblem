"""
Given an array of integers in which two elements appear exactly once and all other 
elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
Follow-up: Can you do this in linear time and constant space?
"""
def singleNumber(nums: List[int]) -> List[int]:
    xor = 0
    for no in nums:
        xor ^= no
    res = [0, 0]
    xor &= -xor
    for no in nums:
        if xor & no == 0:
            res[0] ^= no
        else:
            res[1] ^= no
    return res