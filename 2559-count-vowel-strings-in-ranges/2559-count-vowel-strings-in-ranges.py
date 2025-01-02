class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(["a", "e", "i", "o", "u"])
        prefix = [0] * len(words)
        for i, w in enumerate(words):
            prev = 0
            if i == 0:
                prev = 0
            else:
                prev = prefix[i-1]
            if w[0] in vowel and w[-1] in vowel:
                prev+=1
            prefix[i] = prev
        ans = [0] * len(queries)

        for i, q in enumerate(queries):
            l, r = q[0], q[1]
            if l == 0:
                ans[i] = prefix[r]
            else:
                ans[i] = prefix[r] - prefix[l-1]
        return ans

