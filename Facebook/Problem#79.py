"""
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""
def checkPossibility(nums):
    if len(nums) <= 2:
        return True
    
    count = index = 0
    for i in range(0,len(nums)-1):
        if nums[i] > nums[i+1]:
            index = i
            count += 1
        if count > 1:
            return False
    
    if index ==0  or index == len(nums)-2:
        return True
    return nums[index] <= nums[index+2] or nums[index+1] >= nums[index-1]