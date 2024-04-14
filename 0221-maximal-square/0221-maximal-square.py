class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows,cols = len(matrix), len(matrix[0])
        memo = defaultdict(int)
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols)):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            bottom = dfs(r+1,c)
            right = dfs(r,c+1)
            diagonal = dfs(r+1,c+1)
            if matrix[r][c] == "1":
                memo[(r,c)] = (1 + min(bottom,right,diagonal))
            return memo[(r,c)]
        dfs(0,0)
        return max(memo.values())**2
            
        