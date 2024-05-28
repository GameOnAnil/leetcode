class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        N = len(s)
        res = -1
        for i in range(N):
            for j in range(i,N):
                if s[i] == s[j]:
                    curr = j-i-1
                    res = max(res,curr)

        return res
        