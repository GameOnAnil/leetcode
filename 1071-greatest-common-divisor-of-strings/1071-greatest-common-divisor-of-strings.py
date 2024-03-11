class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        
        gcd = ""
        for i in range(1, len(str2) + 1):
            if len(str2) % i == 0 and len(str1) % i == 0:
                pattern = str2[:i]
                if pattern * (len(str2) // i) == str2 and pattern * (len(str1) // i) == str1:
                    gcd = pattern
        
        return gcd
