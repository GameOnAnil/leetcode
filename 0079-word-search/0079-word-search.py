class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= len(board)
                or c >= len(board[0])
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            left = dfs(r - 1, c, i + 1)
            top = dfs(r, c + 1, i + 1)
            right = dfs(r + 1, c, i + 1)
            bottom = dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return left or right or top or bottom

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
