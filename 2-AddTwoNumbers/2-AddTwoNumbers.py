# Last updated: 11/11/2025, 1:58:17 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        num = num2 = 0
        while l1:
            num += l1.val * i
            i *= 10
            l1 = l1.next  # fix: actually advance

        j = 1
        while l2:
            num2 += l2.val * j
            j *= 10
            l2 = l2.next

        S = num + num2
        s = str(S)

        dummy = ListNode(0)
        cur = dummy
        for ch in s[::-1]:  
            cur.next = ListNode(int(ch))
            cur = cur.next

        return dummy.next
            
        