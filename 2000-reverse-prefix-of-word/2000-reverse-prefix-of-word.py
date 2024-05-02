class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        found = -1
        for i in range(len(word)):
            if ch == word[i]:
                found = i
                break
        if found == -1:
            return word
        first = word[:found+1]
        return first[::-1] + word[found+1:]
        