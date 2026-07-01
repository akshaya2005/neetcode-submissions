# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        
        while left:
            right = left
            i = 0
            while i < k and right:
                right = right.next
                i += 1
            
            if not right or i < k: break
    
            curr = left.next
            prev = right.next
            next = None

            curr = head
            
            curr = head
            prev = right.next
            curr = left.next
            for i in range(k):
                print(curr.val)
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
        
            temp = left.next
            left.next = prev
            left = temp
        
            
            

        
        return dummy.next
            
            
            
            
            



        