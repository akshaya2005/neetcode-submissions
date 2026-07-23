from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ## bfs
        if not node:
            return None
        q = deque()
        visited = {}
        visited[node] = Node(node.val)
        q.append(node)

        while q:
            curr = q.popleft()
            for child in curr.neighbors:
                if child not in visited:
                    q.append(child)
                    newNode = Node(child.val)
                    visited[child] = Node(child.val)
                visited[curr].neighbors.append(visited[child])
            
                
        return visited[node]

                


        