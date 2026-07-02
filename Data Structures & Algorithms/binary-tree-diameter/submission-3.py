# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def helper(root): 
            nonlocal mx
            if not root:
                return 0
            ## the longest path is either conecting two sides or connecting the
            ## top to the bottom

            maxAddableLeftPath = helper(root.left)
            maxAddableRightPath = helper(root.right)
            mx = max(maxAddableLeftPath + maxAddableRightPath, mx)
            return max(maxAddableLeftPath, maxAddableRightPath) + 1
        
        helper(root)
        return mx
        
        