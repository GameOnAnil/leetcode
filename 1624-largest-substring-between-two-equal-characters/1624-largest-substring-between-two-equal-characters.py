class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = defaultdict(list)

        for i, c in enumerate(s):
            seen[c].append(i)
        res = -1
        for i in seen.values():
            curr = max(i) - min(i) -1
            res = max(curr,res)

        return res
        