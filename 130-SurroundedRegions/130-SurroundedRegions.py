# Last updated: 11/11/2025, 1:57:35 AM
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        safe = set()
        visited = set()
        q = collections.deque()
        for r in range(rows):
            if board[r][0] == 'O':
                safe.add((r,0))
                q.append((r,0))
            if board[r][cols-1] == 'O':
                safe.add((r,cols-1))
                q.append((r,cols-1))
        for c in range(cols):
            if board[0][c] == 'O':
                safe.add((0,c))
                q.append((0,c))
            if board[rows-1][c] == 'O':
                safe.add((rows-1, c))
                q.append((rows-1, c))

        while q:
            r, c = q.popleft()
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr,nc) not in visited:
                    safe.add((nr,nc))
                    q.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'


        
                



        