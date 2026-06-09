# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        value = 0
        def helper(root, pred):
            nonlocal value
            if not root:
                return
            if root.val >= pred:
                value += 1
            ## here we want to pick the max of the current pred and root.val
            ## if we directly choose root.val as the new pred we might
            ## end up missing a max value
            helper(root.right, max(pred,root.val))
            helper(root.left, max(pred, root.val))
        helper(root, float('-inf'))
        return value
                