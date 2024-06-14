class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        res = 0
        for i in range(1,N):
            if nums[i] <= nums[i-1]:
                inc = nums[i-1] - nums[i] + 1
                nums[i] = nums[i] + inc
                res+=inc
        return res

        