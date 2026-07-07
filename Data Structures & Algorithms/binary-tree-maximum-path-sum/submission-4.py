# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ## tree dp??
        """
        do an inorder traversal and either include the current node's
        value or exclude it
        """
        globalMaxSum = float('-inf')
        
        def helper(root):
            nonlocal globalMaxSum
            if not root:
                return float('-inf')
            """
            these only return the max path that can be added 
            upwards
            """

            leftMaxPath = helper(root.left)
            rightMaxPath = helper(root.right)
            globalMaxSum = max(leftMaxPath, rightMaxPath, leftMaxPath + rightMaxPath + root.val, globalMaxSum)
            connectableMax = max(leftMaxPath + root.val, rightMaxPath + root.val, root.val)
            print(f"Root={root.val}")
            print(connectableMax, globalMaxSum)
            return connectableMax
        mx = helper(root)
        print(mx, globalMaxSum)
        return max(mx, globalMaxSum)
        """
        six possibilities:
        leftMaxPath + curr + rightMaxPath
        leftMaxPath
        rightMaxPath
        rightMaxPath + curr
        leftMaxPath + curr
        curr -> case where both left max path and right max path are both
        negative
        you can add the leftPathSum and the rightPathSum

        """
