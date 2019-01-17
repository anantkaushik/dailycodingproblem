"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
You can assume the list has at least three integers.
"""
def maximumProduct(nums):
    min1 = min2 = float('inf')
    max1 = max2 = max3 = -float('inf')
    for i in nums:
        if i <= min1:
            min2 = min1
            min1 = i
        elif i <= min2:
            min2 = i
        if i >= max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i >= max2:
            max3 = max2
            max2 = i
        elif i >= max3:
            max3 = i
    return max(min1*min2*max1, max1*max2*max3)