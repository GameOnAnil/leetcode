class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[0 for _ in range(i + 1)] for i in range(numRows)]
        res[0][0] = 1
        for i in range(1, numRows):
            res[i][0] = 1
            for j in range(1, len(res[i])):
                if j < len(res[i - 1]):
                    res[i][j] = res[i - 1][j] + res[i - 1][j - 1]
                else:
                    res[i][j] = 1
        return res
