# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     

        def helper(root):
          
            if not root:
                return 0
            if not root.right and not root.left:
                return 1
            
            return max(helper(root.right), helper(root.left)) + 1
            
        
        return helper(root)

        