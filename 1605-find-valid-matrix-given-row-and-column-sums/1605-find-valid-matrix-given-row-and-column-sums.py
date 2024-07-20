class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N, M = len(rowSum), len(colSum)

        res = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]

        return res
