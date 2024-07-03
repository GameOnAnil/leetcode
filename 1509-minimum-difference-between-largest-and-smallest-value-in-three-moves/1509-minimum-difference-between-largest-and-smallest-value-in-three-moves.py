class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        nums.sort()
        res = float("inf")
        for l in range(4):
            r = N - 4 + l
            res = min(res, abs(nums[r] - nums[l]))
        return res
