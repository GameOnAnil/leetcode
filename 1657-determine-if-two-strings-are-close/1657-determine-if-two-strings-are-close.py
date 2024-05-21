class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        f1, f2 = [0]*26, [0]*26

        for c in word1:
            f1[ord(c) - ord("a")]+=1
        for c in word2:
            f2[ord(c) - ord("a")]+=1

        for i in range(26):
            if (
                (f1[i] == 0 and f2[i] !=0)
                or (f2[i]==0 and f1[i]!= 0)
            ):
            return False

        f1.sort()
        f2.sort()

        for i in range(26):
            if f1[i] != f2[i]:
                return False


        return True

        