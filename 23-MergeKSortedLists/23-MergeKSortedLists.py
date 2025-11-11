# Last updated: 11/11/2025, 1:58:06 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tgt = ListNode()
        tail = tgt
        heap = []
        counter = 0

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, counter, l))
                counter += 1
        
        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return tgt.next
            
            


    


        

                
