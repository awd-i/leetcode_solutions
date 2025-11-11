# Last updated: 11/11/2025, 1:56:56 AM
import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dictionary = defaultdict(list)
        seen = set()
        cc = 0
        for a,b in edges:
            dictionary[a].append(b)
            dictionary[b].append(a)

        def dfs(i):
            seen.add(i)
            for child in dictionary[i]:
                if child not in seen:
                    dfs(child)

        for i in range(n):
            if i not in seen:
                cc += 1
                dfs(i)
        
        return cc


