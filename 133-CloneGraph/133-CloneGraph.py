# Last updated: 11/11/2025, 1:57:33 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[currNode].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]
        