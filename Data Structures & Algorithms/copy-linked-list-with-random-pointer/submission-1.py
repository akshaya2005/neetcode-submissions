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
        ## this one needs a hashmap I think
        nodeToCopy = {}
        curr = head
    
        
        while curr:
            nodeToCopy[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        nodeToCopy[None] = None
        curr = head

        while curr:
            nodeToCopy[curr].next = nodeToCopy[curr.next]
            nodeToCopy[curr].random = nodeToCopy[curr.random]
            curr = curr.next
        
        return nodeToCopy[head]
        

            

            
        

        

        
        