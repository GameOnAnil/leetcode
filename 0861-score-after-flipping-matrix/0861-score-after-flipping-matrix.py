class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Change leftmoset
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] = 1 - grid[i][j]
        
        for j in range(1,cols):
            zero = 0
            ones = 0
            for i in range(rows):
                if grid[i][j] == 0:
                    zero+=1
                else:
                    ones+=1
            if zero > ones:
                for i in range(rows):
                    grid[i][j] = 1 - grid[i][j]
        res = 0
        for i in range(rows):
            for j in range(cols):
                columnScore = grid[i][j] << (cols - j - 1)
                res+=columnScore
        return res
        