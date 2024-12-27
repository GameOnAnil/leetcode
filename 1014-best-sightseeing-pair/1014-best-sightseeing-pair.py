class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        N = len(values)
        best_left = [0] * N
        best_left[0] = values[0]
        for i in range(1, N):
            curr_right = values[i] - i
            ans = max(ans, best_left[i - 1] + curr_right)
            best_left[i] = max(values[i] + i, best_left[i - 1])
        return ans
