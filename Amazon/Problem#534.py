"""
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that 
can form a palindrome.
"""
# Time Complexity: O(N), N -> length of s
# Space Complexity: O(1)
def palindromePermutation(s):
    alphabets = set()
    for c in s:
        if c in alphabets:
            alphabets.remove(c)
        else:
            alphabets.add(c)
    return len(alphabets) <= 1
        