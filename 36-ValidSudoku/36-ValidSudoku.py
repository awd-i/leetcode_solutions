# Last updated: 11/11/2025, 1:58:00 AM
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3, col//3)]:
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[(row//3, col//3)].add(board[row][col])
        return True




        