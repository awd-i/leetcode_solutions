# Last updated: 11/11/2025, 1:57:21 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        numIslands = 0
        
        if not grid:
            return 0

        def dfs(r, c):
            seen.add((r,c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == '1':
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    numIslands += 1
                    dfs(r, c)

        return numIslands