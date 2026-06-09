# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        num1 = 0
        num2 = 0
        base = 1
        while curr1:
            num1 += curr1.val * base
            base *= 10
            curr1 = curr1.next
        base = 1
        while curr2:
            num2 += curr2.val * base
            base *= 10
            curr2 = curr2.next
        res = num1 + num2
        print(num1, num2)
        head = ListNode(0, None)
        if res == 0:
            return head;
        curr = head
        while res > 0:
            digit = res % 10 
            res //= 10
            curr.next = ListNode(digit, None)
            curr = curr.next
        return head.next
    


        