class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)

        countLeftA = 0
        countRightB = s.count("a")
        res = countRightB

        for i in range(N):
            if s[i] == "b":
                countLeftA += 1
            else:
                countRightB -= 1
            res = min(res, countLeftA + countRightB)
        return res
