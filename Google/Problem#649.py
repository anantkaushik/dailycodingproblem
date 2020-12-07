"""
Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""
def firstRepeatedChar(s):
    
    alphabets = set()
    
    for c in s:
      if c in alphabets:
          return c
      alphabets.add(c)
    
    return None
