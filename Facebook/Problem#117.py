"""
Given a binary tree, return the level of the tree with minimum sum.
"""
def minLevelSum(root):
    level = minLevel = 0
    if not root:
        return minLevel

    queue = [[root]]
    minSum = float('inf')
        
    while queue:
        level += 1
        levelNodes = queue.pop(0)
        nextLevel = []
        levelSum = 0
        while levelNodes:
            node = levelNodes.pop()
            levelSum +=node.val
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        if nextLevel:
            queue.append(nextLevel)
        if levelSum < minSum:
            minSum = levelSum
            minLevel = level
    return minLevel
