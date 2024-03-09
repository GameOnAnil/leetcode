class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # Odd
            res = self.check_palindrome(s, i, i, res)
            
            # Even
            res = self.check_palindrome(s, i, i + 1, res)
        return res
    
    def check_palindrome(self, s: str, left: int, right: int, res: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(res):
                res = s[left: right + 1]
            left -= 1
            right += 1
        return res
