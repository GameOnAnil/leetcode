class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        res = 0
        max_res = 0
        while l <= r:
            if tokens[l] <= power:
                res += 1
                power = power - tokens[l]
                l += 1
                max_res = max(res, max_res)
            elif res > 0:
                res -= 1
                power = power + tokens[r]
                r -= 1
            else:
                break
        return max_res
