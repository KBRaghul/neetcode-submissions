# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists
        return lists[0]
    

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        p1 = l1
        p2 = l2

        while p1 and p2:
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        
        tail.next = p1 if p1 else p2

        return dummy.next
        
        