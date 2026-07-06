# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root, greatestVal):
            nonlocal count
            if not root:
                return
            if root.val >= greatestVal:
                greatestVal = root.val
                count += 1
            helper(root.left, greatestVal)
            helper(root.right, greatestVal)
        
        helper(root, root.val)
        return count

        
        