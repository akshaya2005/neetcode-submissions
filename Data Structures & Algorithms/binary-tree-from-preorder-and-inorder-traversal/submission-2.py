# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## preorder = [1,2,3,4]
        ## inorder = [2,1,3,4]
        ## map the inorder list to indices, all the things to the left of an element
        ## on the left side and all the ones to the right are on the right
        indices = defaultdict(int)
        for index, element in enumerate(inorder):
            indices[element] = index
        self.pre_idx = 0
        def helper(l, r):
            if l > r:
                return None
            
            mid = indices[preorder[self.pre_idx]]
            root = TreeNode(preorder[self.pre_idx], None, None)
            self.pre_idx += 1
            root.left = helper(l, mid-1)
            root.right = helper(mid + 1, r)
            return root
        
        return helper(0, len(preorder) - 1)

        


            
            
