"""
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""
class Solution:
    def minPathSum(self, root: TreeNode) -> int:
        self.ans = float('inf')
        
        def helper(root, cur_sum=0):
            if not root:
                self.ans = min(self.ans, cur_sum)
                return 0
            
            cur_sum += root.val
            l = helper(root.left, cur_sum)
            r = helper(root.right, cur_sum)
            cur_sum -= root.val
            
        helper(root)
        
        return self.ans
