# Last updated: 11/11/2025, 1:56:12 AM
import collections
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return None
        rows, cols = len(heights), len(heights[0])
        q = collections.deque()
        q2 = collections.deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        pset = set()
        aset = set()
        visited = set()
        visited2 = set()

        for r in range(rows):
            pset.add((r,0))
            q.append((r,0))
        for c in range(cols):
            pset.add((0,c))
            q.append((0,c))

        for r in range(rows):
            aset.add((r, cols-1))
            q2.append((r,cols-1))
        for c in range(cols):
            aset.add((rows-1, c))
            q2.append((rows-1,c))
                        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:      
                    pset.add((nr,nc))
                    visited.add((nr,nc))
                    q.append((nr,nc))
        
        while q2:
            r, c = q2.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited2:      
                    aset.add((nr,nc))
                    visited2.add((nr,nc))
                    q2.append((nr,nc))
        
        print(pset)
        print(aset)
        
        intersect = aset.intersection(pset)
        return list(intersect)
        


        
                    


