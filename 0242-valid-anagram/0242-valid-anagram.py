class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ds = defaultdict(int)
        dt = defaultdict(int)
        for i in range(len(s)):
            ds[s[i]] += 1
            dt[t[i]] += 1
        return ds == dt
