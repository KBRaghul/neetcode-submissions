# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val < p2.val:
                tail.next = ListNode(p1.val)
                p1 = p1.next
            elif p2.val < p1.val:
                tail.next = ListNode(p2.val)
                p2 = p2.next
            else:
                tail.next = ListNode(p1.val)
                tail = tail.next
                p1 = p1.next
                tail.next = ListNode(p2.val)
                p2 = p2.next
            tail = tail.next

        tail.next = p1 if p1 else p2

        return dummy.next
        
        