class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr = (i+1) ^ nums[i]
            res^=curr
        return res

        