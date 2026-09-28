# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root, maxOnPath):
            nonlocal count
            if not root:
                return
            if maxOnPath <= root.val:
                maxOnPath = root.val
                count += 1
            helper(root.left, maxOnPath)
            helper(root.right, maxOnPath)
        
        helper(root, root.val)
        return count
            
