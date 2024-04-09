class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        res = 0

        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in seen:
                return
            seen.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for i, j in directions:
                bfs(r + i, c + j)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    res += 1
                    bfs(r, c)
        return res
