# Last updated: 11/11/2025, 1:57:31 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        maps = {}
        while curr: # map all the nodes
            maps[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                maps[curr].random = maps[curr.random]
            else:
                maps[curr].random = None
            if curr.next:
                maps[curr].next = maps[curr.next]
            curr = curr.next
        return maps[head]