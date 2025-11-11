# Last updated: 11/11/2025, 1:57:04 AM
import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # tree must be cyclic
        # everything in the tree must be connected
        # len(order) == numCourses

        if len(edges) != (n-1):
            return False

        connections = defaultdict(list)
        
        q = collections.deque()
        
        for a, b in edges:
            connections[b].append(a)
            connections[a].append(b)

        seen = set()
        
        q.append(0)

        while q:
            curr = q.popleft()
            seen.add(curr)
            for child in connections[curr]:
                if child not in seen:
                    q.append(child)
        
        return (len(seen) == n)


        
        