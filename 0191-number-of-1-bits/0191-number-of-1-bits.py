class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            mod = n%2
            res+=mod
            n = n >> 1
        return res
        