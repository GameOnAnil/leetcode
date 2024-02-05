class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        total = 0
        for i in nums:
            if i-1 not in nums:
                j = i + 1
                while j in nums:
                    j+=1
                total = max(total,j-i)
        return total