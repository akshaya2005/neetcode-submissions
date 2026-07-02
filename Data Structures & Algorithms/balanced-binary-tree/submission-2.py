# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return [0, True]
            
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            balanced = leftHeight[1] and rightHeight[1] and abs(leftHeight[0] - rightHeight[0]) <= 1

            return [max(leftHeight[0], rightHeight[0]) + 1, balanced]

        height, balanced = helper(root)
        return balanced
        
        