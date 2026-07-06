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
            left = helper(root.left, prev)
            if prev.val >= root.val:
                return False
            prev.val = root.val
            right = helper(root.right, prev)
            return left and right
        
            
        return helper(root, TreeNode(float('-inf'), None, None))
    

        
        

        