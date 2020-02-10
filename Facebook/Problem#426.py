"""
Given a binary tree, return the level of the tree with minimum sum.
"""
def minLevelSum(root: TreeNode) -> int:
    level = min_level = 0
    if not root:
        return min_level
    queue = [[root]]
    min_sum = float('inf')
    while queue:
        level += 1
        level_nodes = queue.pop(0)
        next_level = []
        level_sum = 0
        while level_nodes:
            node = level_nodes.pop()
            level_sum +=node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            queue.append(next_level)
        if level_sum < min_sum:
            min_sum = level_sum
            min_level = level
    return min_level