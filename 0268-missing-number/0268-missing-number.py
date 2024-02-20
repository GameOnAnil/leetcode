class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for i in nums:
            m = max(i,m)
            if i!=0 and (i-1) not in s:
                return i - 1
        return m + 1

        