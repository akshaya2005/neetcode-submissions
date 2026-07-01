# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1,2,3,4,5,6,7,8
        remove third element from the end


        """
        dummy = ListNode(0, head)
        end = dummy
        for i in range(n):
            end = end.next
        
        curr = dummy
        
        while end.next:
            curr = curr.next
            end = end.next
        curr.next = curr.next.next
        return dummy.next
