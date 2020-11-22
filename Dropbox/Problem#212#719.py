"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""
def convertToTitle(n):
    column_number = 0
    for i in range(len(s)):
        column_number += ((ord(s[-1-i]) - 64) * (26**i))
    return column_number
