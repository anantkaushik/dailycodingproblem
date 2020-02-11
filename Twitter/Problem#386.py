"""
Given a string, sort it in decreasing order based on the frequency of characters. 
If there are multiple possible solutions, return any of them.
For example, given the string tweet, return tteew. eettw would also be acceptable.
"""
def frequencySort(s: str) -> str:
    d1, d2 = {}, {}
    # counter of alphabets
    for c in s:
        d1[c] = d1.get(c, 0) + 1
    
    # make count as key and alphabets as value
    for k,v in d1.items():
        d2[v] = d2.get(v, '') + k*v
    
    res = ''
    for i in range(len(s), -1, -1):
        if i in d2:
            res += d2[i]
    return res