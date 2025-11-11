# Last updated: 11/11/2025, 1:55:59 AM
import collections
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(a,b):
            seen = set()
            stack = [a]
            while stack:
                node = stack.pop()
                seen.add(node)
                if node == b:
                    return True
                for child in graph[node]:
                    if child not in seen:
                        stack.append(child)
            return False

        for u, v in edges:
            if u in graph and v in graph and dfs(u,v):
                return [u,v]
            else:
                graph[u].append(v) # create the graph
                graph[v].append(u)



