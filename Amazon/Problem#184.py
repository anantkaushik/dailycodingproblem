"""
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
"""
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
def greatestDenominator(arr):
    if len(arr) == 1:
        return arr[0]
    gcdd = gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        gcdd = gcd(gcdd,arr[i])
    return gcdd