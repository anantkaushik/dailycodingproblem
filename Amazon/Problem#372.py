"""
Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
"""
# Using Recursion
def countDigit(n): 
    if n == 0: 
        return 0
    return 1 + countDigit(n // 10)

# Using log
# to understand https://math.stackexchange.com/a/231745
# https://stackoverflow.com/a/24177168
import math
def countDigit_using_log(n): 
    return math.floor(math.log(n, 10)+1) 