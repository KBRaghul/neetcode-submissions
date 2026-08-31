# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        front = head
        position = 0

        while front.next and front.next.next:

            
            temp = front.next
            last = self.getLastElement(front)
            front.next = last
            last.next = temp
            front = temp

        
    def getLastElement(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        current = head
        while current.next.next:
            current = current.next

        last = current.next
        current.next = None

        return last



        