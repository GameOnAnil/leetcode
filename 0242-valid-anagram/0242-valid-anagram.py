class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl,tl = list(s),list(t)
        sl.sort()
        tl.sort()
        return sl == tl
        