"""
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
"""
def NthPerfect(n):  
    count = 0
    curr = 19 
    while True:  
        summ = 0 
        x = curr 
        while x > 0: 
            summ = summ + x % 10 
            x //= 10
        if summ == 10:  
            count+=1
        if count == n:  
            return curr 
        curr += 9 
    return -1