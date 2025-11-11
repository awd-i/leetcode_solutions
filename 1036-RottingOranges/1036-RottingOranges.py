# Last updated: 11/11/2025, 1:55:43 AM
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        INF = float('inf')
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxLen = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    grid[r][c] = -1
                if grid[r][c] == 2:
                    grid[r][c] = 0
                    q.append((r,c))
                if grid[r][c] == 1:
                    grid[r][c] = INF
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    return -1
                else:
                    maxLen = max(grid[r][c], maxLen)
        return maxLen
                    



        
        
