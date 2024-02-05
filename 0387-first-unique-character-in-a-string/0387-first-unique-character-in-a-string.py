class Solution:
    def firstUniqChar(self, s: str) -> int:
        di = defaultdict(int)
        for i in s:
            di[i]+=1
        for j in range(len(s)):
            if di[s[j]] == 1:
                return j
        return -1

