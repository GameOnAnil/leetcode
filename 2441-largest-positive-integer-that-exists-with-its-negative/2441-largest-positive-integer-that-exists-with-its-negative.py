class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        res = -1
        for n in nums:
            if -n in nums:
                res = max(res,abs(n))
        return res

        