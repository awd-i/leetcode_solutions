# Last updated: 11/11/2025, 1:57:32 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        if head is None:
            return False
        if head.next is None:
            return False
        
        while head is not None:
            if head.next in seen:
                return True
            else:
                seen.add(head.next)
                head = head.next
        return False

        