class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = nums[0]
        for i in nums:
            curSum += i
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
        return res
