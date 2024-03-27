class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(["a", "e", "i", "o", "u"])
        res, l, r = 0, 0, k
        for i in range(k):
            if s[i] in vowel:
                res += 1
        curr = res
        while r < len(s):
            if s[r] in vowel:
                curr += 1
            if s[l] in vowel:
                curr -= 1
            res = max(res, curr)
            l += 1
            r += 1
        return res
