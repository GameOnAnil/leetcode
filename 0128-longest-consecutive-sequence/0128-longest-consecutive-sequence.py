class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in data:
            if i - 1 not in nums:
                j = i + 1
                while j in nums:
                    j += 1
                res = max(j - i, res)
        return res
