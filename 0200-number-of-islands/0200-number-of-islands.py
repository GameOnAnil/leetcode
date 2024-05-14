class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c]!="1"
            ):
                return
            direction  = ((1,0),(-1,0),(0,1),(0,-1))
            grid[r][c]="#"
            for i , j in direction:
                dfs(r+i,c+j)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res+=1
                    dfs(r,c)
        return res

        