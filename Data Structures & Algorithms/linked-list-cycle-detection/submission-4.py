# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head

        while slow and fast:
            if fast.next==None or slow.next==None:
                return False
            fast=fast.next.next
            slow=slow.next
            if not slow or not fast:
                return False
            if fast.val==slow.val and fast.next==slow.next:
                return True
            
        return False