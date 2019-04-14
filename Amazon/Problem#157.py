"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.
"""
def isPalindrome(s):
    temp = set()
    for c in s:
        if c in temp:
            temp.remove(c)
        else:
            temp.add(c)
    return len(temp) <= 1