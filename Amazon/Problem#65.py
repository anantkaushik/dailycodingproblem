"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""
def spiralOrder(matrix):
    if matrix == []:
        return []
    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    direction = 0
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left,right+1):
                print(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top,bottom+1):
                print(matrix[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                print(matrix[i][left])
            left += 1
        direction = (direction+1) % 4