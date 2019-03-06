"""
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""
def sortedSquares(A):
    l = len(A)
    j = 0
    while j < l and A[j] < 0:
        j += 1
    i = j - 1
    res = []
    while i >= 0 and j < l:
        if A[i]**2 < A[j]**2:
            res.append(A[i]**2)
            i -= 1
        else:
            res.append(A[j]**2)
            j += 1
    while i >= 0:
        res.append(A[i]**2)
        i -= 1
    while j < l:
        res.append(A[j]**2)
        j += 1
    return res