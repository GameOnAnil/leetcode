class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        res = 0
        oddExists = False
        for c in count.values():
            if (c % 2) == 0:
                res = res + c
            else:
                res = res + c - 1
                oddExists = True
        return res + 1 if oddExists else res
