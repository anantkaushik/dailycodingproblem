"""
Write a program to merge two binary trees. Each node in the new tree should hold a 
value equal to the sum of the values of the corresponding nodes of the input trees.
If only one input tree has a node in a given position, the corresponding node in 
the new tree should match that input node.
"""
def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 or not t2:
        return t1 or t2
    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1
