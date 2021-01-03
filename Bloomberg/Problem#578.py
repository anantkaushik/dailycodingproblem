"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""
def isIsomorphic(s, t):
    d1 , d2 = {}, {}
    
    for i in range(len(s)):
        if d1.get(ord(s[i]),-1) != d2.get(ord(t[i]),-1):
            return False
    
    d1[ord(s[i])] = i
    d2[ord(t[i])] = i
    
    return True
        