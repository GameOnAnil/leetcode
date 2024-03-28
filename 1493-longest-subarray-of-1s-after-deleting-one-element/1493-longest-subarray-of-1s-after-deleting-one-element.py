class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, k = 0, 1
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k +=1 - nums[l]
                l += 1
        return r - l
