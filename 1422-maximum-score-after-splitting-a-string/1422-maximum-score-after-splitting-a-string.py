class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        prefix = [0] * N
        suffix = [0] * N

        for i in range(N):
            left = prefix[i - 1] if i > 0 else 0
            if s[i] == "0":
                left += 1
            prefix[i] = left
        print(prefix)

        for i in range(N - 1, -1, -1):
            right = suffix[i + 1] if i < N - 1 else 0
            if s[i] == "1":
                right += 1
            suffix[i] = right
        print(suffix)
        ans = 0
        for i in range(N - 1):
            ans = max(ans, prefix[i] + suffix[i + 1])
        return ans
