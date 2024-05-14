class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c]!=1):
                return 0
            direction = ((1,0),(-1,0),(0,1),(0,-1))
            curr = 1
            grid[r][c]=0
            for i, j in direction:
                curr+=dfs(r+i,c+j)
            return curr


        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    curr = dfs(r,c)
                    print("CURR",r,c,curr)
                    res = max(curr,res)
        return res

        