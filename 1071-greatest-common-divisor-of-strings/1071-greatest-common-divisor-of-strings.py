class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1 % i or len2 % i:
                continue
            base = str1[:i]
            n1 = len1 // i
            n2 = len2 // i
            if str1 == n1 * base and str2 == n2 * base:
                return base
        return ""
