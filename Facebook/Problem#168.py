"""
Given an N by N matrix, rotate it by 90 degrees clockwise.
For example, given the following matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""
def rotate(matrix):
    l = len(matrix)
    for layer in range(l//2):
        first,last = layer, l-1-layer
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top