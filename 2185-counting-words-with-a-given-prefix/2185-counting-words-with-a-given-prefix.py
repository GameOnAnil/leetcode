class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        def isPrefix(s1,s2):
            if len(s1) < len(s2):
                return False
            for i in range(len(s2)):
                if s1[i] != s2[i]:
                    return False
            return True

        for w in words:
            if isPrefix(w,pref):
                res+=1
        return res
        