class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        seen = [[0] * (N * 3) for _ in range(N * 3)]

        for i in range(N):
            for j in range(N):
                r = i * 3
                c = j * 3
                if grid[i][j] == "/":
                    seen[r][c + 2] = 1
                    seen[r + 1][c + 1] = 1
                    seen[r + 2][c] = 1
                elif grid[i][j] == "\\":
                    seen[r][c] = 1
                    seen[r + 1][c + 1] = 1
                    seen[r + 2][c + 2] = 1

        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                i, j = stack.pop()
                if 0 <= i < N * 3 and 0 <= j < N * 3 and seen[i][j] == 0:
                    seen[i][j] = 1
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        stack.append((i + dx, j + dy))

        res = 0
        for i in range(N * 3):
            for j in range(N * 3):
                if seen[i][j] == 0:
                    dfs(i, j)
                    res += 1

        return res
