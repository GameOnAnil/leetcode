class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        res = ""
        while index < len(word1) or index < len(word2):
            if len(word1) > index:
                res += word1[index]
            if len(word2) > index:
                res += word2[index]
            index += 1
        return res
