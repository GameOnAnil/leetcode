class Solution:
    def maxDepth(self, s: str) -> int:
        currMax = 0
        start = end = 0
        for i in range(len(s)):
            if s[i] == "(":
                start+=1
            if s[i] == ")":
                end+=1
                start-=1
            currMax = max(start,currMax)
        return currMax
        