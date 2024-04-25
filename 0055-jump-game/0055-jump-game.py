class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        l, r = len(nums) - 2, len(nums) - 1
        while l >= 0:
            if (l + nums[l]) >= r:
                r = l
            l-=1
        return r == 0
