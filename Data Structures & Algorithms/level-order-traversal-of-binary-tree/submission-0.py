# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            qlen = len(queue)
            l = []
            for i in range(qlen):
                elem = queue.popleft()
                if elem:
                    l.append(elem.val)
                    queue.append(elem.left)
                    queue.append(elem.right)
            res.append(l)              
        
        res.pop()
        return res