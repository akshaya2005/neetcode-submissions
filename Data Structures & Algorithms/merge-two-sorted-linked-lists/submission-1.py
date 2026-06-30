# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2

        head = ListNode(None, None)
        curr = head

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                curr.next = pointer1
                pointer1 = pointer1.next
            else:
                curr.next = pointer2
                pointer2 = pointer2.next
            curr = curr.next
        
        while pointer1:
            curr.next = pointer1
            pointer1 = pointer1.next
            curr = curr.next
        
        while pointer2:
            curr.next = pointer2
            pointer2 = pointer2.next
            curr = curr.next
        

        return head.next
        




        