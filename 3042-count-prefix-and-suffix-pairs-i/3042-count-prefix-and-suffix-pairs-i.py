class Solution:
    def isPrefix(self, str1, str2):
        if len(str2) < len(str1):
            return False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True

    def isSuffix(self, str1, str2):
        if len(str2) < len(str1):
            return False
        length = len(str1)
        for i in range(len(str1)):
            if str1[len(str1) - i - 1] != str2[len(str2) - i - 1]:
                return False
        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        N = len(words)
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                if self.isSuffix(words[i], words[j]) and self.isPrefix(
                    words[i], words[j]
                ):
                    res += 1
        return res
