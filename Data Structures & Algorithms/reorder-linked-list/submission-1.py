# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## use hashmap
        ## or reverse the second half of the list and then connect the
        ## nodes accordingly

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        prev = None
        nxt = None

        
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # slow.next = prev
        p2 = prev
        p1 = head

        nxt1 = None
        nxt2 = None
        while p1 and p2:
            nxt1 = p1.next
            nxt2 = p2.next
            p1.next = p2
            p2.next = nxt1
            p1 = nxt1
            p2 = nxt2

        """
        2, 4, 6.    10, 8
        """
        