class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,prod,res = 0, 1, 0
        for r in range(len(nums)):
            prod*=nums[r]
            while prod >=k and l<=r:
                prod/=nums[l]
                l+=1
            res += r - l + 1
        return res