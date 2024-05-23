class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        left, right= 0, sum(nums)
        for i, v in enumerate(nums):
            right-=v
            if left == right:
                return i
            left+=v
        return -1

        