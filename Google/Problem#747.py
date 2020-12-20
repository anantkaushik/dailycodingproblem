"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""
def is_rotation(A, B):
    if len(A) != len(B):
        return False

    return B in A + A
