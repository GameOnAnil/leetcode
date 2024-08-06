class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0]*26

        for w in word:
            count[ord(w)-ord("a")]+=1

        count.sort(reverse=True)
        res = 0
        for i in range(26):
            if count[i] == 0:
                break
            res += (i//8+1) * count[i]
        return res

        