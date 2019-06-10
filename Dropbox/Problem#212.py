"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""
def convertToTitle(n):
    col = []
    while n:
        n = n-1
        col.append(chr((n%26)+65))
        n=n//26
    return "".join(col[::-1])