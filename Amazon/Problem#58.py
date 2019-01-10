"""
An sorted array of integers was rotated an unknown number of times.
Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.
For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
You can assume all the integers in the array are unique.
"""
def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        elif nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return None # If element not present in the array.