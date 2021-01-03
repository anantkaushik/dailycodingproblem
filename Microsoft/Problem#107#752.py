"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""
def traverse_level_order(root):
    if not root:
        return []
        
    current, res = [root], []
        
    while current:
        nex, temp = [], []

        for n in current:
            temp.append(n.val)
            if n.left:
                nex.append(n.left)
            if n.right:
                nex.append(n.right)

        current = nex
        res.append(temp)
        
    return res
  
