class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        for i in d.values():
            if i != 0:
                return False
        return True
