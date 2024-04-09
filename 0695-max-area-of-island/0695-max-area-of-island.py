class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or
                grid[r][c] != 1):
                return 0
            grid[r][c] = "#"
            directions = [(1,0),(-1,0),(0,1),(0,-1),]
            curr = 0
            for i, j in directions:
                curr +=dfs(r+i,c+j)
            return 1 + curr
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr = dfs(r,c)
                    res = max(curr,res)
        return res
