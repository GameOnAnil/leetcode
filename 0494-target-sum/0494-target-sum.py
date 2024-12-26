class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        @cache
        def choose(i, curr_sum, isPositive):
            if i == len(nums):
                return 1 if curr_sum == target else 0
            positive = choose(i + 1, curr_sum + nums[i], True)
            negative = choose(i + 1, curr_sum - nums[i], False)
            return positive + negative

        p = choose(1, 0 + nums[0], True)
        n = choose(1, 0 - nums[0], False)
        return p + n
