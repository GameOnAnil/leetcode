class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        10,15,20
        """
        N = len(cost)
        for i in range(N-3,-1,-1):
            # print(i)
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
        