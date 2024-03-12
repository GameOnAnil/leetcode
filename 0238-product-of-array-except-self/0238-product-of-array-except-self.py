class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre , suf = 1, 1
        for i in range(len(nums)):
            res[i] *= pre
            pre = pre * nums[i]
            res[-1 - i] *= suf
            suf *= nums[-1 - i]
        return res
