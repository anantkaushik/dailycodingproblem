"""
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.
For example, given [1, 2, 1, 1, 3, 4, 1], return 1.
"""
def majorityElement(nums):
    c,ans = 0,0
    for i in nums:
        if c == 0:
            c+=1
            ans = i
        elif ans == i:
            c += 1
        else:
            c -= 1
    return ans