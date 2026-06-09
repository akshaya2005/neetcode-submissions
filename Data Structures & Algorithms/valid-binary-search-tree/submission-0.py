# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, prev):      
            if not root:
                return True
            if not helper(root.left, prev):
                return False
            
            if root.val <= prev.val:
                return False
            prev.val = root.val
            
            if not helper(root.right, prev):
                return False
            return True
        return helper(root, TreeNode(float('-inf'), None, None))

        