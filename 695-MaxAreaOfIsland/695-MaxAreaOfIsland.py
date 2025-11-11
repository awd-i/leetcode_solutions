# Last updated: 11/11/2025, 1:55:57 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        maxLen = 0
        

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            size = 1
            size += dfs(r - 1, c)
            size += dfs(r, c - 1)
            size += dfs(r + 1, c)
            size += dfs(r, c + 1)
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxLen = max(maxLen, dfs(r,c))
        
        return maxLen