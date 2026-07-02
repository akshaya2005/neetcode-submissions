# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False

            leftTreesSame = isSameTree(p.left, q.left)
            rightTreesSame = isSameTree(p.right, q.right)

            return leftTreesSame and rightTreesSame
        
        def helper(root):
            
            if not root:
                return False
            print(f"Root val: {root.val}")
            isSame = False
            if root.val == subRoot.val:
                isSame = isSameTree(root, subRoot)
            
            
            if isSame:
                return True
            else:
                return helper(root.right) or helper(root.left)
            
        
        return helper(root)
        
            