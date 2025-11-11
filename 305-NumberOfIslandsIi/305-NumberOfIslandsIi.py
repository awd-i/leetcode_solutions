# Last updated: 11/11/2025, 1:56:58 AM
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        seen,pa,res,count = set(), {}, [], 0
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        def find(x):
            while x in pa:
                if pa[x] in pa:
                    pa[x] = pa[pa[x]]
                x = pa[x]
            return x
        def union(x,y):
            pax, pay=find(x), find(y)
            if pax == pay:
                return False
            pa[pax] = pay
            return True
        for x, y in positions:
            if (x,y) not in seen:
                seen.add((x,y))
                count += 1
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    if (nr, nc) in seen and union((nr, nc),(x,y)):
                        count -= 1
            res.append(count)
        return res