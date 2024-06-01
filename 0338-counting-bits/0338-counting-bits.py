class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0 -> 0
        2 -> 1 + dp[2-2]
        4 -> 1 + dp[4-4]
        8 -> 1 + dp[8-8]
        16 -> 1 + dp[16-16]
        """
        dp = [0] * (n+1)
        offset = 2 ** 0
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]

        return dp
        