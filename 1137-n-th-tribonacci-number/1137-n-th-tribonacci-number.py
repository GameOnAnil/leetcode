class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        seen = [0]*(n+1)
        seen[0] = 0
        seen[1] = 1
        seen[2] = 1
        if n <=2:
            return seen[n]
        for i in range(2,n+1):
            seen[i] = seen[i-1] + seen[i-2] + seen[i-3]
        return seen[n]
