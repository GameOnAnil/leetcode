class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for i, j in directions:
                bfs(r + i, c + j)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        return res
