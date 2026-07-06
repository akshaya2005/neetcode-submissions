# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        q = deque()
        if not root:
            return []
        q.append(root)
        while q:
            qsize = len(q)
            currLevel = []
            node = None
            for i in range(qsize):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            array.append(node.val)
        
        return array

        