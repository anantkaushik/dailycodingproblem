"""
Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.
"""
def isPalindrome_alternative(x):
    # If no is negative
    # If last digit is 0 and no is not 0
    if x < 0  or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = (rev*10) + (x%10)
        x //= 10
    # When the length is an odd number, we can get rid of the middle digit by rev/10
    return rev == x or rev//10 == x