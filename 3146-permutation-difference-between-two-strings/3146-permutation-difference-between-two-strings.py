class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        seen = {}
        for i in range(len(s)):
            seen[s[i]]=i
        res = 0
        for i in range(len(t)):
            res+=abs(seen[t[i]]-i) 
        return res
