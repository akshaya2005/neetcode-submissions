# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = 0
        def helper(root):
            nonlocal length
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            length = max(l+r, length)

            return 1 + max(l, r)
        helper(root)
        return length