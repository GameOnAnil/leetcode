class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        res = ""
        while index < len(word1) and index < len(word2):
            res = res + word1[index] + word2[index]
            index += 1
        if len(word1) > index:
            res += word1[index:]
        if len(word2) > index:
            res += word2[index:]
        return res
