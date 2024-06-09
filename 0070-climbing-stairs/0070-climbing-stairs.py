class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] *( n + 1)
       
        def solve(i):
            if i == 0 or i == 1:
                return 1
            if dp[i]!=-1:
                return dp[i]
            curr = solve(i-1) + solve(i-2)
            dp[i] = curr
            return curr

        return solve(n)


        

        