# Last updated: 11/11/2025, 1:56:59 AM
import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms is None or rooms[0] is None:
            return None
        q = collections.deque()
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr,nc))
                

        