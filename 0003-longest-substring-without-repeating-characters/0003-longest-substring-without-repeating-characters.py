class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        l,result = 0, 0
        for r in range(len(s)):
            while s[r] in subSet:
                subSet.remove(s[l])
                l+=1
            subSet.add(s[r])
            result = max(result,r-l+1)
        return result
        