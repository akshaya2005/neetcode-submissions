"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None:None}
        cur = head
        ## map old node to new Node
        while cur:
            hm[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            hm[cur].next = hm[cur.next]
            hm[cur].random = hm[cur.random]
            cur = cur.next
        return hm[head]