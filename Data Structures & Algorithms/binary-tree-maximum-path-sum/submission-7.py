# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def helper(curr):
            nonlocal maxSum
        
            if curr == None:
                return float('-inf')
            
            maxLeft = helper(curr.left)
            maxRight = helper(curr.right)
            total = maxLeft + curr.val + maxRight
            maxConnectable = max(maxLeft + curr.val, maxRight + curr.val, curr.val)
            maxSum = max(maxSum, maxLeft, maxRight, total, maxConnectable)
            return maxConnectable
        
        mx = helper(root)
        return max(mx, maxSum)
        