class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N)
        dp[-2] = cost[-2]
        dp[-1] = cost[-1]
        
        for i in range(N-3,-1,-1):
            dp[i] = min(cost[i] + dp[i+1],cost[i] + dp[i+2])

        return min(dp[0],dp[1])
        