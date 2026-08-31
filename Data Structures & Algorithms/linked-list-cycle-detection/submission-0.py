# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hset = set()
        fast = head

        while fast:
            if fast in hset:
                return True

            hset.add(fast)
            fast = fast.next

        return False