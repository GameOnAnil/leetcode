class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v <= 0:
                nums[i] = 0
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if index in range(len(nums)):
                # if 0 set to -inf
                if nums[index] == 0:
                    nums[index] = -inf
                # if positive change to negative
                # need to check this because we can have duplicate
                elif nums[index] > 0:
                    nums[index] *= -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1
