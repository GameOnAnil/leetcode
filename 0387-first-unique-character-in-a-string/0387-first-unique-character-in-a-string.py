class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i , v in enumerate(s):
            if v in seen:
                continue
            hasMatch = False
            seen.add(v)
            for j in range(i + 1, len(s)):
                if s[j] == v:
                    hasMatch = True
            if not hasMatch:
                return i
        return -1

