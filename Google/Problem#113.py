"""
Given a string of words delimited by spaces, reverse the words in string. 
For example, given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation in-place?
"""
def reverseWords(s):
    s = list(s)
    startIndex = 0
    endIndex = len(s)-1
    while s[startIndex] == ' ':
        startIndex += 1
    while s[endIndex] == ' ':
        endIndex -= 1
        
    start = startIndex
    end = start
    for i in range(startIndex,endIndex+1):
        if s[i] == ' ':
            reverseWord(s,start,end-1)
            start = end+1
            end += 1
    reverseWord(s,start,end-1)
    reverseWord(s,startIndex,endIndex)
    return "".join(s[startIndex:endIndex+1])
    
def reverseWord(s,start,end):
    while start < end:
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1
            