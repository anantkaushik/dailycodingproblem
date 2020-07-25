"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""
def twoSum(arr,target):
    n = set()
    for i in arr:
        temp = target - i
        if temp in n:
            return True
        n.add(i)
    return False
