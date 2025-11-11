# Last updated: 11/11/2025, 1:55:39 AM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return None
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        directions = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
        q = deque()
        q.append((0,0,1))
        visited = {(0,0)}
        target = (rows-1, cols-1)
        while q:
            r, c, d = q.popleft()
            if (r, c) == target:
                return d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc)) # check visited here
                    q.append((nr, nc, d+1))
        return -1
            



    

