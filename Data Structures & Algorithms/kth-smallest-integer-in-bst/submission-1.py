# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = TreeNode(0, None, None)
        count = 0
        def helper(root, k):
            nonlocal count, node
            if not root or count == k:
                return
            
            helper(root.left, k)
            count += 1
            if count == k:
                node.val = root.val
                return
            if count < k:
                helper(root.right, k)
        
        helper(root, k)
        return node.val

        