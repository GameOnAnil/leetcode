class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        l, r = 0, 0

        for r in range(len(s)):
            right_diff = abs(ord(s[r]) - ord(t[r]))
            maxCost -= right_diff
            while maxCost < 0:
                left_diff = abs(ord(s[l]) - ord(t[l]))
                maxCost += left_diff
                l += 1
            res = max(res, r - l + 1)

        return res
