"""
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.
"""
def isPalindrome(x):
    if x < 0:
        return False
    rev = 0
    temp = x
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp //= 10
    return True if rev == x else False