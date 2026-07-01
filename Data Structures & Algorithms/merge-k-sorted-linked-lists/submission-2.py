# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        k = len(lists)
        empty = 0
        while True:
            minIndex = 0
            while minIndex < len(lists) and not lists[minIndex]:
                minIndex += 1
            for i in range(k):
                if lists[i] and lists[i].val < lists[minIndex].val:
                    minIndex = i
            if minIndex == len(lists):
                break
        
            curr.next = ListNode(lists[minIndex].val, None)
            lists[minIndex] = lists[minIndex].next
            curr = curr.next
        return dummy.next
                
                

