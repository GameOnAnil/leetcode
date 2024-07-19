class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        INF = 10**6
        row_min = [INF]*rows
        col_max =[-INF]*cols
        for r in range(rows):
            for c in range(cols):
                row_min[r] = min(row_min[r],matrix[r][c])
                col_max[c] = max(col_max[c],matrix[r][c])

        res = list(set(row_min)&set(col_max))
        return res        