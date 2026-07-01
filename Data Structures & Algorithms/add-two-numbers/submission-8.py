# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        carry = 0
        while l1 and l2:
            t = l1.val + l2.val + carry
            val = t % 10
            carry = t // 10
            curr.next = ListNode(val, None)
            curr = curr.next
            l1, l2 = l1.next, l2.next
        while l1:
            t = l1.val + carry
            carry = t // 10
            val = t % 10
            curr.next = ListNode(val, None)
            curr = curr.next
            l1 = l1.next
        while l2:
            t = l2.val + carry
            carry = t // 10
            val = t % 10
            curr.next = ListNode(val, None)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(1, None)

        return dummy.next



