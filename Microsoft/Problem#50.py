"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one 
of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
"""
def evaluate(root): 
    if root is None: 
        return 0
    if root.left is None and root.right is None: 
        return int(root.data) 
    leftSum = evaluate(root.left) 
    rightSum = evaluate(root.right) 
    if root.data == '+': 
        return leftSum + rightSum 
    elif root.data == '-': 
        return leftSum - rightSum 
    elif root.data == '*': 
        return leftSum * rightSum 
    elif root.data == '/' :
        return leftSum // rightSum 