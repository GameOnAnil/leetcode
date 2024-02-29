class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            curMax = 0
            while l <= r:
                curMax = max(l + nums[l], curMax)
                l += 1
            l, r = r + 1, curMax
            res += 1
        return res
