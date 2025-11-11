# Last updated: 11/11/2025, 1:57:47 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1) or
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1)
            )
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                        return True
        return False

        
        