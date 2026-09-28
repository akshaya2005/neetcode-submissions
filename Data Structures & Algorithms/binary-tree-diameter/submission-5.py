# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxPath = 0
        
        def helper(root):
            nonlocal maxPath
            
            if not root:
                return -1
            
            if not root.right and not root.left:
                return 0
            ## return the max connectable path
            left = helper(root.left)
            right = helper(root.right)
            print(root.val)
            print("best connectable paths")
            print(left, right)

            maxPath = max(maxPath, left + right + 2, left + 1, right + 1)
            print(f"maxPath: {maxPath}")
            return max(left + 1, right + 1)
        helper(root)
        return maxPath

                

        