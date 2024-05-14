class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(r,c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == 0
            ):
                return 0
            temp = grid[r][c]
            grid[r][c]=0
            right = dfs(r+1,c)
            left = dfs(r-1,c)
            bot = dfs(r,c+1)
            top = dfs(r,c-1)
            grid[r][c] = temp
            return max(left,right,bot,top) + temp

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    continue
                currSum = dfs(r,c)
                res = max(currSum,res)

        return res

        