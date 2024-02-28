class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDiagonal = set()
        nDiagonal = set()
        board = [["."] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in pDiagonal or (r - c) in nDiagonal:
                    continue
                col.add(c)
                pDiagonal.add(r + c)
                nDiagonal.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                col.remove(c)
                pDiagonal.remove(r + c)
                nDiagonal.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
