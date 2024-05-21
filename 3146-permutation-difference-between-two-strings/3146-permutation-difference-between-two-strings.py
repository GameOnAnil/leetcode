class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res=0
        for i, c in enumerate(s):
            res+=abs(i-t.index(c))
        return res
