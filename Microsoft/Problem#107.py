"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""
def traverse_level_order(root):
    q = [root]
    while q:
        temp = q.pop(0)
        print(temp.data,end=' ')
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)