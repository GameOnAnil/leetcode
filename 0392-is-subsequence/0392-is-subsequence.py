class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (not s and not t) or (not s and t):
            return True
        if not t and s:
            return False
        l = 0
        for i in t:
            if l >=len(s):
                break
            print(s[l], i)
            if s[l] == i:
                l += 1
        return l >= len(s)
